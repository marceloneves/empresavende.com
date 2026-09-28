// Redireciona www.empresavende.com -> empresavende.com (301), recebe o formulário
// de contato (POST /contato, enviado por e-mail pelo Resend) e serve o site estático.
//
// Secret: RESEND_API_KEY (npx wrangler secret put RESEND_API_KEY).
// Vars (wrangler.jsonc): EMAIL_FROM (remetente do domínio verificado no Resend), CONTATO_TO.

function text(value, max) {
  return String(value ?? '').trim().slice(0, max)
}

function escapeHtml(value) {
  return value.replace(/[&<>"']/g, (char) => `&#${char.charCodeAt(0)};`)
}

async function contato(request, env) {
  const url = new URL(request.url)
  const back = (status) => Response.redirect(`${url.origin}/#contato-${status}`, 303)

  const form = await request.formData()
  // Campo-armadilha preenchido: robô. Responde "ok" para não ensinar o robô.
  if (text(form.get('website'), 200)) return back('ok')

  const name = text(form.get('name'), 120)
  const company = text(form.get('company'), 120)
  const phone = text(form.get('phone'), 30)
  const email = text(form.get('email'), 200).toLowerCase()
  const message = text(form.get('message'), 2000)
  const validEmail = !email || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
  if (!name || phone.replace(/\D/g, '').length < 8 || !validEmail) return back('erro')

  const rows = [
    ['Nome', name],
    ['Empresa', company],
    ['WhatsApp', phone],
    ['E-mail', email],
    ['Mensagem', message],
  ].filter(([, value]) => value)
  const html = rows
    .map(([label, value]) => `<p><b>${label}:</b><br>${escapeHtml(value).replace(/\n/g, '<br>')}</p>`)
    .join('')
  const plain = rows.map(([label, value]) => `${label}: ${value}`).join('\n\n')

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: env.EMAIL_FROM,
        to: [env.CONTATO_TO],
        ...(email ? { reply_to: email } : {}),
        subject: `Contato pelo site — ${name}${company ? ` (${company})` : ''}`,
        html,
        text: plain,
      }),
    })
    if (!response.ok) {
      console.error('resend', response.status, await response.text())
      return back('erro')
    }
  } catch (error) {
    console.error('resend', error)
    return back('erro')
  }
  // Sem JS na página: a âncora mostra a mensagem de retorno (CSS :target).
  return back('ok')
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url)
    if (url.hostname.startsWith('www.')) {
      url.hostname = url.hostname.slice(4)
      return Response.redirect(url.toString(), 301)
    }
    if (url.pathname === '/contato' && request.method === 'POST') {
      return contato(request, env)
    }
    return env.ASSETS.fetch(request)
  },
}

// Vercel serverless function: emails contact form submissions via Resend.
// Set these in Vercel > Project > Settings > Environment Variables:
//   RESEND_API_KEY  - from resend.com (verify thatfoodielawyer.com there first)
//   CONTACT_TO      - foodie@thatfoodielawyer.com
//   CONTACT_FROM    - e.g. "TFL Website <website@thatfoodielawyer.com>"
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const { name = '', email = '', organization = '', topic = '', message = '', website = '' } = req.body || {};
  if (website) return res.status(200).json({ ok: true }); // honeypot
  if (!name.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || !message.trim()) {
    return res.status(400).json({ error: 'Missing fields' });
  }
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const html = `<h2>New enquiry from thatfoodielawyer.com</h2>
<p><b>Name:</b> ${esc(name)}<br><b>Email:</b> ${esc(email)}<br><b>Organization:</b> ${esc(organization) || '-'}<br><b>Interested in:</b> ${esc(topic)}</p>
<p style="white-space:pre-wrap">${esc(message)}</p>`;
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: process.env.CONTACT_FROM,
      to: [process.env.CONTACT_TO || 'foodie@thatfoodielawyer.com'],
      reply_to: email,
      subject: `Website enquiry: ${topic} from ${name}`.slice(0, 150),
      html,
    }),
  });
  if (!r.ok) return res.status(502).json({ error: 'Email failed' });
  return res.status(200).json({ ok: true });
}

# That Foodie Lawyer website

Static site (HTML/CSS/JS) built from the "TFL Website Copy, Designer-Ready Revision" doc.
Pages: Home, About, Global Consulting, Experiences, Ideas, Contact, plus Book a Strategy Call and 404.

Design samples for the client: `samples.html` links Sample A (the full site), Sample B (`option-b.html`, editorial) and Sample C (`option-c.html`, bold yellow). B and C are homepage-only until she picks one.
Original photos stay in `photos/` and are not deployed; web versions are in `site/assets/img/`.

## Structure
- `src/build.py`: all page content lives here. Edit it, then run `python3 src/build.py` to regenerate `site/*.html`.
- `site/`: the deployable site (deploy this folder to Vercel as the project root).
- `site/api/contact.js`: Vercel function that emails contact-form messages via Resend.
- `site/vercel.json`: clean URLs and redirects from the old Wix paths.

## Before launch
1. **Calendly + Stripe (booking and payment)**
   - Calendly plan must be Standard or higher to take payments.
   - In Calendly: Integrations & apps > Stripe > connect her Stripe account (live mode).
   - Create the event "Food & Hospitality Strategy Call", 45 min, video location (Zoom/Google Meet).
   - Event > More options > Payment: turn on "Require payment to book", Stripe, 249, CAD. Add payment/cancellation terms.
   - Add booking questions (business name, what to focus on).
   - Paste the event link into `CALENDLY_URL` in `src/build.py` and rebuild. Until then the page shows an "email to book" fallback.
   - She gets booking notifications by email from Calendly and payouts in Stripe.
2. **Contact form**: verify thatfoodielawyer.com in Resend, then set `RESEND_API_KEY`, `CONTACT_TO`, `CONTACT_FROM` in Vercel env vars.
3. **Domain**: add thatfoodielawyer.com + www in Vercel, update DNS where the domain is registered (currently pointing at Wix). Keep her email (MX records) untouched.
4. **Needs from Azeezat**
   - Approval of the draft copy on Experiences and Ideas (not in the copy doc).
   - Blog posts to migrate from Wix; article cards on Ideas link to `#` for now.
   - Social media links (footer has a slot).
   - Flodesk: once she decides, paste the embed code where `FLODESK` is marked in `footer()` in build.py.
5. Strategy Call price ($249 CAD) is marked editable pending final approval.

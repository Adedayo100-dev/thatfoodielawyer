# That Foodie Lawyer website

Static site (HTML/CSS/JS) built from the "TFL Website Copy, Designer-Ready Revision" doc, in the "Signature" design (Sample C) chosen by Azeezat.
Pages: Home, About, Global Consulting, Experiences, Ideas, Contact, Book a Strategy Call, 404.

## Structure
- `src/build.py`: all page content lives here. Edit it, then run `python src/build.py` to regenerate `site/*.html`.
- `site/`: the deployable site. On Netlify set **Base directory** to `site` (no build command).
- `site/netlify.toml`: redirects from old Wix paths and caching.
- Contact form uses **Netlify Forms** (free tier). Submissions appear in Netlify > Forms; turn on email notifications to foodie@thatfoodielawyer.com.
- Original photos stay in `photos/` (git-ignored); web versions are in `site/assets/img/`.

## Before launch
1. **Calendly + Stripe**: upgrade her Calendly to Standard, connect Stripe (live mode), use Google Meet as the location. Create one paid event per core offer (Strategy Call $199/45 min, Growth Readiness Audit $650/90 min, Implementation Sprint $1,500, Advisory Partnership $1,997 first month) and paste each link into `src/offers.py`, then rebuild.
2. **Netlify**: deploy, then Forms > enable form detection, and add a notification email.
3. **Domain (GoDaddy) and email (Google Workspace)**: Wix shows the domain as "managed by third party, connected by DNS", so DNS is at GoDaddy. At launch, only change the website records (A / CNAME for @ and www) to Netlify's. Never touch the MX or TXT records (her Google email).
4. Wix: Premium Basic plan, billed monthly, next charge Nov 16, 2026. Cancel only after the new site and email are confirmed working.

## Still needed from Azeezat
- Blog posts to migrate from Wix (Ideas article cards link to `#` for now).
- Her own Experiences and Ideas copy (current copy is interim, approved for now).
- HST, cancellation/refund policy, availability for each bookable offer.
- A That Foodie Lawyer logo, if separate from the TFL Global Consulting logo.

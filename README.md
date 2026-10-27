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
1. **Calendly + Stripe**: upgrade her Calendly from Basic to Standard (needed to take payments), connect Stripe (live mode, confirm her bank is linked). Create ONE paid event: "Food & Hospitality Strategy Call", 45 min, $249 CAD (she is not HST-registered, so no tax), location Google Meet.
   - Policy text: "Payments are non-refundable. You can reschedule up to 48 hours before your call."
   - Availability (Toronto time): Thu 8-10 PM; Fri 7-9 PM; Sat 11 AM-1 PM, 1:30-3:30 PM, 7-9 PM; Sun 11:30 AM-1:30 PM, 5-7 PM.
   - Paste the event link into `calendly` for the Strategy Call in `src/offers.py`, then rebuild.
   - Other offers are recommended after the call, so they have no price or booking. Partnership months 2 and 3 are billed by her through Stripe.
2. **Netlify**: Forms detection on, email notification to foodie@thatfoodielawyer.com (done).
3. **Domain (GoDaddy) and email (Google Workspace)**: Wix shows the domain as "managed by third party, connected by DNS", so DNS is at GoDaddy (Dayo has delegate access). At launch, only change the website records (A / CNAME for @ and www) to Netlify's. Never touch the MX or TXT records (her Google email).
4. Wix: Premium Basic plan, billed monthly, next charge Nov 16, 2026. Cancel only after the new site and email are confirmed working.

## Still needed from Azeezat
- Blog posts to migrate from Wix (Ideas article cards link to `#` for now).
- Her own Experiences and Ideas copy (current copy is interim, approved for now).
- Google Business Profile (not verified yet): link the site once it is.
- A That Foodie Lawyer logo, if separate from the TFL Global Consulting logo.

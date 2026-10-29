# That Foodie Lawyer website

Static site (HTML/CSS/JS) built from the "TFL Website Copy, Designer-Ready Revision" doc, in the "Signature" design (Sample C) chosen by Azeezat.
Pages: Home, About, Global Consulting, Experiences, Ideas, Contact, Book a Strategy Call, 404.

## Structure
- `src/build.py`: page content. `src/offers.py`: consulting offers. `src/blog.py`: turns blog posts into pages.
- `content/posts/*.md`: blog posts (one file per post). Azeezat edits these through the blog editor at `/admin`.
- `site/`: the published website. `site/admin/`: the Decap CMS blog editor and its settings (`config.yml`).
- `netlify.toml` (repo root): Netlify runs `pip install -r requirements.txt && python3 src/build.py`, then publishes `site/`.
  In Netlify, **Base directory must be empty**, publish directory `site`.
- To build on your PC: `pip install -r requirements.txt`, then `python src/build.py`.
- Contact form uses **Netlify Forms**; notifications go to foodie@thatfoodielawyer.com.
- Original photos stay in `photos/` (git-ignored); web versions are in `site/assets/img/`.

## Blog editor (Decap CMS)
- One-time setup: GitHub OAuth app (callback `https://api.netlify.com/auth/done`), installed in Netlify under Project configuration > Security > OAuth > GitHub.
- Azeezat needs a free GitHub account added as a collaborator (Write access) on the repo.
- She logs in at `/admin`, writes a post, clicks Publish. Netlify rebuilds and the post is live in about a minute.
- Cover photos of any size are resized to web versions automatically during the build.

## Newsletter (Kit, free plan)
- Signup boxes appear on the Ideas page, every blog post and the footer once `KIT_FORM_ID` is set in `src/build.py` (hidden while empty).
- New posts are emailed manually: in Kit, create a Broadcast with the post title, 1-2 lines and a link. RSS feed for automation later: `/feed.xml`.

## Before launch
1. **Calendly + Stripe**: upgrade her Calendly from Basic to Standard (needed to take payments), connect Stripe (live mode, confirm her bank is linked). Create ONE paid event: "Food & Hospitality Strategy Call", 45 min, $249 CAD (she is not HST-registered, so no tax), location Google Meet.
   - Policy text: "Payments are non-refundable. You can reschedule up to 48 hours before your call."
   - Availability (Toronto time): Thu 8-10 PM; Fri 7-9 PM; Sat 11 AM-1 PM, 1:30-3:30 PM, 7-9 PM; Sun 11:30 AM-1:30 PM, 5-7 PM.
   - Paste the event link into `calendly` for the Strategy Call in `src/offers.py`, then rebuild.
   - Other offers are recommended after the call, so they have no price or booking. Partnership months 2 and 3 are billed by her through Stripe.
2. **Netlify**: Forms detection on, email notification to foodie@thatfoodielawyer.com (done).
3. **Domain and DNS**: the domain is *registered* at GoDaddy (Dayo has delegate access), but its *nameservers point to Wix* (ns0/ns1.wixdns.net), so all DNS records, including her Google Workspace email, currently live in **Wix DNS**. Plan: move DNS to Cloudflare first (copy every record below), then transfer the registration from GoDaddy to Cloudflare, then cancel Wix.
   Current records (read Oct 27, 2026). Keep the email ones exactly:
   | Type | Name | Value | Notes |
   |---|---|---|---|
   | MX | @ | aspmx.l.google.com (priority 10) | Google email |
   | MX | @ | alt1.aspmx.l.google.com (20) | Google email |
   | MX | @ | alt2.aspmx.l.google.com (30) | Google email |
   | MX | @ | alt3.aspmx.l.google.com (40) | Google email |
   | MX | @ | alt4.aspmx.l.google.com (50) | Google email |
   | TXT | @ | v=spf1 include:_spf.google.com -all | email sender check |
   | TXT | @ | google-site-verification=gSGJk3V7FJ8P3qxJ9WMdOPKfxlr9NiAuyKAvPqLt_jY | Google ownership |
   | TXT | _dmarc | v=DMARC1; p=none | email policy |
   | A | @ | 185.230.63.x (Wix) | REPLACE with 75.2.60.5 (Netlify), DNS only |
   | CNAME | www | cdn3.wixdns.net (Wix) | REPLACE with thatfoodielawyer.netlify.app, DNS only |
   No DKIM record (google._domainkey) exists yet; worth adding later from Google Admin for better email delivery.
4. Wix: Premium Basic plan, billed monthly, next charge Nov 16, 2026. Cancel only after the new site and email are confirmed working.

## Still needed from Azeezat
- Decide whether the 5 Jollof Concert event photos go into that post.
- Her own Experiences and Ideas copy (current copy is interim, approved for now).
- Google Business Profile (not verified yet): link the site once it is.
- A That Foodie Lawyer logo, if separate from the TFL Global Consulting logo.

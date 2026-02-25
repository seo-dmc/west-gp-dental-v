import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))

SERVICES = [
    ('invisalign-grande-prairie.html','Invisalign'),
    ('dental-implants-grande-prairie.html','Dental Implants'),
    ('emergency-dentist-grande-prairie.html','Emergency Dentist'),
    ('family-dentist-grande-prairie.html','Family Dentist'),
    ('teeth-whitening-grande-prairie.html','Teeth Whitening'),
    ('root-canal-grande-prairie.html','Root Canal'),
    ('dental-veneers-grande-prairie.html','Dental Veneers'),
    ('dentures-grande-prairie.html','Dentures'),
    ('sedation-dentistry-grande-prairie.html','Sedation Dentistry'),
    ('wisdom-teeth-removal-grande-prairie.html','Wisdom Teeth Removal'),
    ('dental-crowns-grande-prairie.html','Dental Crowns'),
    ('childrens-dentist-grande-prairie.html','Childrens Dentist'),
    ('cosmetic-dentist-grande-prairie.html','Cosmetic Dentist'),
    ('botox-grande-prairie.html','Botox'),
    ('tmj-treatment-grande-prairie.html','TMJ Treatment'),
    ('dental-bridges-grande-prairie.html','Dental Bridges'),
    ('sleep-apnea-dentist-grande-prairie.html','Sleep Apnea'),
    ('mouth-guards-grande-prairie.html','Mouth Guards'),
    ('dental-hygiene-grande-prairie.html','Dental Hygiene'),
    ('all-on-4-dental-implants-grande-prairie.html','All-on-4 Implants'),
]

AREAS = [
    ('downtown-T8V 3A3.html','Downtown'),
    ('westgate-T8V 4K5.html','Westgate'),
    ('eastgate-T8V 6H2.html','Eastgate'),
    ('southgate-T8V 7M9.html','Southgate'),
    ('northgate-T8V 2B1.html','Northgate'),
    ('riverheights-T8V 5E4.html','Riverheights'),
    ('montrose-T8V 1G7.html','Montrose'),
    ('elmwood-T8V 3J2.html','Elmwood'),
    ('braeside-T8V 4P8.html','Braeside'),
    ('crystal-heights-T8V 6L5.html','Crystal Heights'),
    ('highland-park-T8V 8N3.html','Highland Park'),
    ('avondale-T8V 2H6.html','Avondale'),
    ('country-club-estates-T8V 7K1.html','Country Club Estates'),
    ('mission-heights-T8V 5R4.html','Mission Heights'),
    ('buckingham-T8V 3M7.html','Buckingham'),
]

CSS = """<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Maven Pro',sans-serif;color:#616161;background:#fff;}
a{text-decoration:none;transition:color .2s;}
.dd,.dd2{display:none;position:absolute;top:100%;left:0;background:#fff;
  min-width:220px;box-shadow:0 8px 24px rgba(0,0,0,.12);border-radius:10px;
  padding:8px 0;z-index:999;max-height:360px;overflow-y:auto;}
.nav-item:hover .dd,.nav-item:hover .dd2{display:block;}
.dd a,.dd2 a{display:block;padding:9px 18px;font-size:13px;color:#1a1a2e;}
.dd a:hover,.dd2 a:hover{background:#f0fafb;color:#26c6da;}
.prose p,.prose ul li{color:#616161;line-height:1.75;margin-bottom:.9em;}
.prose h2{font-family:'Playfair Display',serif;font-size:1.6rem;color:#115278;
  margin:1.4em 0 .5em;font-weight:700;}
.prose h3{font-size:1.2rem;color:#115278;margin:1.2em 0 .4em;font-weight:700;}
.prose ul{padding-left:1.4em;margin-bottom:1em;}
.prose strong{color:#115278;}
.prose table{width:100%;border-collapse:collapse;margin:1.2em 0;}
.prose th{background:#e8f8fa;border:1px solid #c8e8ef;padding:9px 14px;
  text-align:left;color:#115278;font-weight:700;}
.prose td{border:1px solid #d0edf2;padding:9px 14px;}
/* Benefit grid cards */
.benefit-card{background:#f0fafb;border-radius:10px;padding:16px 18px;
  display:flex;align-items:flex-start;gap:14px;margin-bottom:14px;}
.benefit-icon{width:32px;height:32px;border-radius:50%;background:#26c6da;
  color:#fff;display:flex;align-items:center;justify-content:center;
  font-size:14px;flex-shrink:0;}
/* Process steps */
.step{display:flex;align-items:flex-start;gap:14px;margin-bottom:20px;}
.step-num{width:38px;height:38px;border-radius:50%;background:#115278;
  color:#fff;display:flex;align-items:center;justify-content:center;
  font-weight:700;flex-shrink:0;}
.step-bar{height:6px;border-radius:3px;background:#e0e0e0;margin-top:8px;}
.step-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,#26c6da,#115278);}
@media(max-width:768px){
  .nav-desktop{display:none!important;}
  .maps-grid{grid-template-columns:1fr!important;}
}
</style>"""

MAPS_HTML = """<section style="padding:60px 0;background:#f0fafb;">
<div style="max-width:1220px;margin:0 auto;padding:0 20px;">
<h2 style="font-family:'Playfair Display',serif;font-size:36px;color:#26c6da;
  text-align:center;margin-bottom:10px;">Our Locations</h2>
<p style="text-align:center;color:#616161;margin-bottom:30px;">
  Visit us at any of our convenient Grande Prairie locations.</p>
<div class="maps-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px;">
<div style="border-radius:14px;overflow:hidden;height:280px;border:3px solid #e8f8fa;">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2278.690644981913!2d-118.8441848!3d55.1711883!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5390916472c1eb19%3A0x35da25af7ded9426!2sWest%20Grande%20Prairie%20Dental%20-%20Westgate!5e0!3m2!1sen!2sca!4v1770372276920!5m2!1sen!2sca"
width="100%" height="100%" style="border:0;" allowfullscreen loading="lazy"></iframe></div>
<div style="border-radius:14px;overflow:hidden;height:280px;border:3px solid #e8f8fa;">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d18222.891808925062!2d-118.84091815948159!3d55.185692842838996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x539095f38e205133%3A0xcd113d0e9f5659a5!2sWest%20Grande%20Prairie%20Dental%20-%20Trader%20Ridge!5e0!3m2!1sen!2sca!4v1770372312769!5m2!1sen!2sca"
width="100%" height="100%" style="border:0;" allowfullscreen loading="lazy"></iframe></div>
</div>
<div style="border-radius:14px;overflow:hidden;height:260px;border:3px solid #e8f8fa;">
<iframe src="https://www.google.com/maps/d/embed?mid=1QyfgRUzzGTsBkUw0Ticscf_fI35Qlmk"
width="100%" height="100%" style="border:0;"></iframe></div>
</div></section>"""

FOOTER_HTML = """<footer style="background:linear-gradient(135deg,#26c6da 0%,#1ab2c5 100%);padding:55px 0 0;">
<div style="max-width:1220px;margin:0 auto;padding:0 20px;">
<div style="display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:36px;margin-bottom:36px;flex-wrap:wrap;">
<div>
  <div style="font-family:'Maven Pro',sans-serif;font-size:20px;font-weight:700;
    color:#fff;margin-bottom:12px;">West GP<span style="color:#115278;">Dental</span></div>
  <p style="font-size:14px;color:rgba(255,255,255,.85);line-height:1.7;margin-bottom:10px;">
    Modern dentistry for the whole family in Grande Prairie, AB.</p>
  <p style="font-size:13px;color:rgba(255,255,255,.85);margin-bottom:6px;">
    &#128222; (780) 833-8600</p>
  <p style="font-size:13px;color:rgba(255,255,255,.85);">
    &#128205; 11502 Westgate Dr #106, Grande Prairie, AB T8V 4E9</p>
</div>
<div>
  <h4 style="font-weight:700;color:#115278;font-size:15px;margin-bottom:14px;">Services</h4>
  <a href="services/invisalign-grande-prairie.html" style="display:block;font-size:13px;color:rgba(255,255,255,.85);margin-bottom:7px;">Invisalign</a>
  <a href="services/dental-implants-grande-prairie.html" style="display:block;font-size:13px;color:rgba(255,255,255,.85);margin-bottom:7px;">Dental Implants</a>
  <a href="services/emergency-dentist-grande-prairie.html" style="display:block;font-size:13px;color:rgba(255,255,255,.85);margin-bottom:7px;">Emergency Dentist</a>
  <a href="services/teeth-whitening-grande-prairie.html" style="display:block;font-size:13px;color:rgba(255,255,255,.85);margin-bottom:7px;">Teeth Whitening</a>
  <a href="services/dental-crowns-grande-prairie.html" style="display:block;font-size:13px;color:rgba(255,255,255,.85);margin-bottom:7px;">Dental Crowns</a>
  <a href="services/cosmetic-dentist-grande-prairie.html" style="display:block;font-size:13px;color:rgba(255,255,255,.85);margin-bottom:7px;">Cosmetic Dentist</a>
</div>
<div>
  <h4 style="font-weight:700;color:#115278;font-size:15px;margin-bottom:14px;">Working Hours</h4>
  <div style="font-size:13px;color:rgba(255,255,255,.85);line-height:2.1;">
    Mon &ndash; Fri: 8AM &ndash; 6PM<br/>
    Saturday: 9AM &ndash; 5PM<br/>
    Sunday: Closed<br/><br/>
    <strong style="color:#115278;">24/7 Emergencies:</strong><br/>(780) 833-8600
  </div>
</div>
</div>
<div style="border-top:1px solid rgba(255,255,255,.2);padding:16px 0;text-align:center;">
<p style="font-size:13px;color:rgba(255,255,255,.7);">
  &copy; 2025 West Grande Prairie Dental. All rights reserved.</p>
</div></div></footer>"""


def make_header(prefix):
    svc = "".join(
        f'<a href="{prefix}services/{f}">{n}</a>'
        for f, n in SERVICES
    )
    ar = "".join(
        f'<a href="{prefix}areas-we-serve/{f}">{n}</a>'
        for f, n in AREAS
    )
    return f"""<div style="background:#115278;color:rgba(255,255,255,.85);font-size:13px;padding:6px 20px;">
  &#128336; Mon-Fri: 8AM-6PM &nbsp;|&nbsp; Sat: 9AM-5PM
  &nbsp;&nbsp;&#128205; 11502 Westgate Dr #106, Grande Prairie, AB T8V 4E9
</div>
<header style="background:#fff;box-shadow:0 2px 12px rgba(0,0,0,.08);position:sticky;top:0;z-index:1000;">
<div style="max-width:1220px;margin:0 auto;padding:0 20px;display:flex;
  align-items:center;justify-content:space-between;height:70px;">
  <a href="{prefix}index.html" style="font-family:'Maven Pro',sans-serif;font-size:20px;
    font-weight:700;text-decoration:none;">
    <span style="color:#115278;">West GP</span><span style="color:#26c6da;">Dental</span>
  </a>
  <nav class="nav-desktop" style="display:flex;gap:26px;align-items:center;position:relative;">
    <a href="{prefix}index.html" style="color:#115278;font-weight:600;font-size:14px;">Home</a>
    <div class="nav-item" style="position:relative;">
      <span style="color:#115278;font-weight:600;font-size:14px;cursor:pointer;">Services &#9660;</span>
      <div class="dd">{svc}</div>
    </div>
    <div class="nav-item" style="position:relative;">
      <span style="color:#115278;font-weight:600;font-size:14px;cursor:pointer;">Areas &#9660;</span>
      <div class="dd2">{ar}</div>
    </div>
    <a href="{prefix}blog/index.html" style="color:#115278;font-weight:600;font-size:14px;">Blog</a>
    <a href="{prefix}index.html#contact" style="color:#115278;font-weight:600;font-size:14px;">Contact</a>
  </nav>
  <a href="tel:(780) 833-8600" style="background:#115278;color:#fff;padding:10px 20px;
    border-radius:50px;font-size:14px;font-weight:700;text-decoration:none;">
    &#128222; (780) 833-8600
  </a>
</div>
</header>"""


def restyle(fp, prefix):
    with open(fp, 'r', encoding='utf-8', errors='ignore') as fh:
        c = fh.read()
    title_m = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
    desc_m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']', c, re.IGNORECASE)
    title = title_m.group(1).strip() if title_m else 'West Grande Prairie Dental'
    desc = desc_m.group(1).strip() if desc_m else 'West Grande Prairie Dental - Professional dental care in Grande Prairie, AB.'
    body_m = re.search(r'<body[^>]*>(.*?)</body>', c, re.DOTALL)
    if not body_m:
        print(f'  SKIP (no body): {fp}')
        return
    body = body_m.group(1)
    # Strip old nav/header – keep only <main> or <section> content
    body = re.sub(r'^[\s\S]*?(?=<main\b|<section\b|<article\b)', '', body, flags=re.DOTALL)
    # Strip old footer + footers
    body = re.sub(r'<footer[\s\S]*?</footer>', '', body)
    # Strip leftover <nav>
    body = re.sub(r'<nav\b[\s\S]*?</nav>', '', body)
    # Clean up mobile-menu inline scripts
    body = re.sub(r'<script>\(function\(\)\{try.*?\}\)\(\);</script>', '', body, flags=re.DOTALL)
    short_title = re.sub(r'\s*[|\-\u2013\u2014].*', '', title).strip()

    new_html = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<meta charset="UTF-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n'
        f'<title>{title}</title>\n'
        f'<meta name="description" content="{desc}"/>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700'
        '&amp;family=Maven+Pro:wght@400;600;700&amp;display=swap" rel="stylesheet"/>\n'
        f'{CSS}\n'
        '</head>\n<body>\n'
        f'{make_header(prefix)}\n'
        '<main>\n'
        '<div style="background:linear-gradient(135deg,#26c6da 0%,#1ab2c5 100%);\n'
        '  padding:56px 20px;text-align:center;">\n'
        '<div style="display:inline-block;background:rgba(255,255,255,.2);color:#fff;\n'
        '  padding:6px 18px;border-radius:50px;font-size:12px;font-weight:700;margin-bottom:14px;">\n'
        'West Grande Prairie Dental</div>\n'
        f'<h1 style="font-family:\'Playfair Display\',serif;font-size:38px;color:#fff;margin-bottom:8px;">'
        f'{short_title}</h1>\n'
        '<p style="color:rgba(255,255,255,.9);font-size:15px;">Grande Prairie, AB &mdash; (780) 833-8600</p>\n'
        '</div>\n'
        '<div style="max-width:900px;margin:0 auto;padding:50px 20px;" class="prose">\n'
        f'{body}\n'
        '</div>\n'
        f'{MAPS_HTML}\n'
        '</main>\n'
        f'{FOOTER_HTML}\n'
        '</body>\n</html>'
    )

    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(new_html)
    print(f'  OK: {os.path.basename(fp)}')


count = 0
for pattern in ['services/*.html', 'areas-we-serve/*.html', 'blog/*.html']:
    folder = pattern.split('/')[0]
    print(f'\n-- {folder} --')
    for fp in sorted(glob.glob(os.path.join(BASE, pattern))):
        restyle(fp, '../')
        count += 1

print(f'\nDONE! {count} files restyled.')

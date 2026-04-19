nodes_data = [
    {'id': 'FORTRAN', 'year': 1957, 'category': 'Procedural'},
    {'id': 'COBOL', 'year': 1959, 'category': 'Procedural'},
    {'id': 'ALGOL 60', 'year': 1960, 'category': 'Procedural'},
    {'id': 'ALGOL 68', 'year': 1968, 'category': 'Procedural'},
    {'id': 'Pascal', 'year': 1970, 'category': 'Procedural'},
    {'id': 'BCPL / B', 'year': 1969, 'category': 'Procedural'},
    {'id': 'C', 'year': 1972, 'category': 'Procedural'},
    {'id': 'Ada', 'year': 1980, 'category': 'Procedural'},
    {'id': 'Go', 'year': 2009, 'category': 'Procedural'},
    {'id': 'Rust', 'year': 2010, 'category': 'Procedural'},
    {'id': 'Zig', 'year': 2016, 'category': 'Procedural'},
    {'id': 'Simula 67', 'year': 1967, 'category': 'OOP'},
    {'id': 'Smalltalk', 'year': 1972, 'category': 'OOP'},
    {'id': 'C++', 'year': 1983, 'category': 'OOP'},
    {'id': 'Objective-C', 'year': 1984, 'category': 'OOP'},
    {'id': 'Eiffel', 'year': 1985, 'category': 'OOP'},
    {'id': 'Java', 'year': 1995, 'category': 'OOP'},
    {'id': 'Delphi', 'year': 1995, 'category': 'OOP'},
    {'id': 'C#', 'year': 2000, 'category': 'OOP'},
    {'id': 'D', 'year': 2001, 'category': 'OOP'},
    {'id': 'Scala', 'year': 2004, 'category': 'OOP'},
    {'id': 'Kotlin', 'year': 2011, 'category': 'OOP'},
    {'id': 'Swift', 'year': 2014, 'category': 'OOP'},
    {'id': 'Lisp', 'year': 1958, 'category': 'Functional'},
    {'id': 'Scheme', 'year': 1975, 'category': 'Functional'},
    {'id': 'ML', 'year': 1973, 'category': 'Functional'},
    {'id': 'Standard ML', 'year': 1984, 'category': 'Functional'},
    {'id': 'Haskell', 'year': 1990, 'category': 'Functional'},
    {'id': 'OCaml', 'year': 1996, 'category': 'Functional'},
    {'id': 'Julia', 'year': 2012, 'category': 'Functional'},
    {'id': 'BASIC', 'year': 1964, 'category': 'Procedural'},
    {'id': 'Perl', 'year': 1987, 'category': 'Scripting'},
    {'id': 'Python', 'year': 1991, 'category': 'Scripting'},
    {'id': 'Ruby', 'year': 1995, 'category': 'Scripting'},
    {'id': 'PHP', 'year': 1994, 'category': 'Scripting'},
    {'id': 'Lua', 'year': 1993, 'category': 'Scripting'},
    {'id': 'JavaScript', 'year': 1995, 'category': 'Scripting'},
    {'id': 'TypeScript', 'year': 2012, 'category': 'Scripting'},
    {'id': 'Self', 'year': 1986, 'category': 'Scripting'},
    {'id': 'CSP', 'year': 1978, 'category': 'Concurrent'},
    {'id': 'Erlang', 'year': 1986, 'category': 'Concurrent'},
    {'id': 'Limbo', 'year': 1995, 'category': 'Concurrent'},
    {'id': 'Elixir', 'year': 2011, 'category': 'Concurrent'}
]

links_data = [
    # --- 実線（直接の派生・発展） ---
    {'source': 'FORTRAN', 'target': 'ALGOL 60', 'type': 'solid'},
    {'source': 'ALGOL 60', 'target': 'ALGOL 68', 'type': 'solid'},
    {'source': 'ALGOL 60', 'target': 'Pascal', 'type': 'solid'},
    {'source': 'ALGOL 60', 'target': 'BCPL / B', 'type': 'solid'},
    {'source': 'BCPL / B', 'target': 'C', 'type': 'solid'},
    {'source': 'ALGOL 68', 'target': 'C', 'type': 'solid'},
    {'source': 'Pascal', 'target': 'Ada', 'type': 'solid'},
    {'source': 'Pascal', 'target': 'Delphi', 'type': 'solid'},
    {'source': 'C', 'target': 'C++', 'type': 'solid'},
    {'source': 'C', 'target': 'Objective-C', 'type': 'solid'},
    {'source': 'C', 'target': 'Java', 'type': 'solid'},
    {'source': 'C', 'target': 'C#', 'type': 'solid'},
    {'source': 'C', 'target': 'Go', 'type': 'solid'},
    {'source': 'C', 'target': 'D', 'type': 'solid'},
    {'source': 'C', 'target': 'Zig', 'type': 'solid'},
    {'source': 'Simula 67', 'target': 'Smalltalk', 'type': 'solid'},
    {'source': 'Simula 67', 'target': 'C++', 'type': 'solid'},
    {'source': 'Smalltalk', 'target': 'Objective-C', 'type': 'solid'},
    {'source': 'Smalltalk', 'target': 'Ruby', 'type': 'solid'},
    {'source': 'C++', 'target': 'Java', 'type': 'solid'},
    {'source': 'C++', 'target': 'C#', 'type': 'solid'},
    {'source': 'C++', 'target': 'D', 'type': 'solid'},
    {'source': 'Objective-C', 'target': 'Swift', 'type': 'solid'},
    {'source': 'Java', 'target': 'Scala', 'type': 'solid'},
    {'source': 'Java', 'target': 'Kotlin', 'type': 'solid'},
    {'source': 'Lisp', 'target': 'Scheme', 'type': 'solid'},
    {'source': 'ML', 'target': 'Standard ML', 'type': 'solid'},
    {'source': 'Standard ML', 'target': 'OCaml', 'type': 'solid'},
    {'source': 'Standard ML', 'target': 'Haskell', 'type': 'solid'},
    {'source': 'JavaScript', 'target': 'TypeScript', 'type': 'solid'},
    {'source': 'CSP', 'target': 'Erlang', 'type': 'solid'},
    {'source': 'CSP', 'target': 'Limbo', 'type': 'solid'},
    {'source': 'Erlang', 'target': 'Elixir', 'type': 'solid'},
    
    # --- 点線（強い影響・概念の継承） ---
    {'source': 'Smalltalk', 'target': 'Self', 'type': 'dashed'},
    {'source': 'Lisp', 'target': 'ML', 'type': 'dashed'},
    {'source': 'Scheme', 'target': 'Standard ML', 'type': 'dashed'},
    {'source': 'Haskell', 'target': 'Scala', 'type': 'dashed'},
    {'source': 'Self', 'target': 'JavaScript', 'type': 'dashed'},
    {'source': 'Perl', 'target': 'Python', 'type': 'dashed'},
    {'source': 'Perl', 'target': 'Ruby', 'type': 'dashed'},
    {'source': 'Perl', 'target': 'PHP', 'type': 'dashed'},
    {'source': 'Python', 'target': 'Julia', 'type': 'dashed'},
    {'source': 'C', 'target': 'Rust', 'type': 'dashed'},
    {'source': 'OCaml', 'target': 'Rust', 'type': 'dashed'}, 
    {'source': 'C++', 'target': 'Rust', 'type': 'dashed'},   
    {'source': 'Scheme', 'target': 'JavaScript', 'type': 'dashed'}, 
    {'source': 'Ruby', 'target': 'Elixir', 'type': 'dashed'},
    {'source': 'Java', 'target': 'C#', 'type': 'dashed'},
    {'source': 'Haskell', 'target': 'Rust', 'type': 'dashed'},
    {'source': 'Delphi', 'target': 'C#', 'type': 'dashed'},
    {'source': 'COBOL', 'target': 'Ada', 'type': 'dashed'},
    {'source': 'Limbo', 'target': 'Go', 'type': 'dashed'},
    {'source': 'Pascal', 'target': 'Go', 'type': 'dashed'},
    {'source': 'C', 'target': 'Limbo', 'type': 'dashed'},
    {'source': 'Rust', 'target': 'Swift', 'type': 'dashed'}  # ★追加: 現代の安全性重視言語としての相互影響
]

width, height = 1600, 1050
padding = 80
rect_w, rect_h = 96, 32
margin_x, track_h = 40, 45

cat_colors = {
    'Procedural': '#4a7cba', 'OOP': '#55a049', 'Functional': '#d4a017',
    'Scripting': '#8e44ad', 'Concurrent': '#c0392b'
}

def get_x(year):
    return padding + (year - 1950) * (width - 2 * padding) / (2025 - 1950)

cat_y = {
    'Procedural': 180, 'OOP': 380, 'Functional': 580,
    'Scripting': 780, 'Concurrent': 940
}

node_pos = {}
cat_tracks = {cat: {} for cat in cat_y.keys()}
sorted_nodes = sorted(nodes_data, key=lambda n: n['year'])

for node in sorted_nodes:
    cat = node['category']
    base_x, base_y = get_x(node['year']), cat_y[cat]
    best_track = 0
    for track in [0, -1, 1, -2, 2, -3, 3]:
        if base_x > cat_tracks[cat].get(track, -1000) + rect_w + margin_x:
            best_track = track
            break
    cat_tracks[cat][best_track] = base_x
    node_pos[node['id']] = (base_x, base_y + best_track * track_h)

out_dict = {n['id']: [] for n in nodes_data}
in_dict = {n['id']: [] for n in nodes_data}
for l in links_data:
    out_dict[l['source']].append(l)
    in_dict[l['target']].append(l)

def assign_ports(links, is_source):
    links.sort(key=lambda x: node_pos[x['target' if is_source else 'source']][1])
    count = len(links)
    for i, l in enumerate(links):
        offset = 0 if count <= 1 else -10 + i * (20 / (count - 1))
        l['sy_offset' if is_source else 'ey_offset'] = offset

for nid in out_dict: assign_ports(out_dict[nid], True)
for nid in in_dict: assign_ports(in_dict[nid], False)

def is_clear(sx, sy, ex, ey, sid, tid):
    steps = int(max(abs(ex - sx), abs(ey - sy)) / 5)
    if steps <= 1: return True
    px, py = rect_w/2 + 10, rect_h/2 + 10
    for i in range(1, steps):
        t = i / steps
        tx, ty = sx + (ex - sx) * t, sy + (ey - sy) * t
        for n in nodes_data:
            if n['id'] in [sid, tid]: continue
            nx, ny = node_pos[n['id']]
            if nx - px < tx < nx + px and ny - py < ty < ny + py: return False
    return True

svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
svg += f'<title>プログラミング言語 進化の系譜</title>\n'
svg += f'<rect width="{width}" height="{height}" fill="#fafbfc" />\n'
svg += '<defs><marker id="as" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#5a6c7d"/></marker>'
svg += '<marker id="ad" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#8b9bac"/></marker></defs>\n'

for l in links_data:
    sx, sy = node_pos[l['source']][0] + rect_w/2, node_pos[l['source']][1] + l['sy_offset']
    ex, ey = node_pos[l['target']][0] - rect_w/2, node_pos[l['target']][1] + l['ey_offset']
    dx = ex - sx
    h_len = max(60, dx * 0.4) if dx >= 80 else max(60, abs(sy - ey) * 0.5)
    
    if is_clear(sx, sy, ex, ey, l['source'], l['target']) or abs(sy - ey) > 20:
        path = f"M{sx},{sy}C{sx+h_len},{sy} {ex-h_len},{ey} {ex},{ey}"
    else:
        mx, my = (sx+ex)/2, (sy+ey)/2 + 45 * (-1 if hash(l['source'])%2==0 else 1)
        path = f"M{sx},{sy}C{sx+dx*0.25},{sy} {mx-dx*0.25},{my} {mx},{my}C{mx+dx*0.25},{my} {ex-dx*0.25},{ey} {ex},{ey}"
    
    dash = 'stroke-dasharray="4,4"' if l['type'] == 'dashed' else ''
    color = '#8b9bac' if l['type'] == 'dashed' else '#5a6c7d'
    m_id = 'ad' if l['type'] == 'dashed' else 'as'
    svg += f'<path d="{path}" stroke="{color}" stroke-width="1.4" fill="none" {dash} marker-end="url(#{m_id})" opacity="0.7"/>\n'

for decade in range(1950, 2030, 10):
    tx = get_x(decade)
    svg += f'<line x1="{tx}" y1="80" x2="{tx}" y2="{height-80}" stroke="#e1e4e8" stroke-width="1"/><text x="{tx}" y="45" text-anchor="middle" font-size="16" font-family="sans-serif" fill="#95a5a6" font-weight="bold">{decade}s</text>\n'

for cat, y in cat_y.items():
    svg += f'<text x="30" y="{y}" transform="rotate(-90 30 {y})" font-size="14" font-family="sans-serif" fill="{cat_colors[cat]}" font-weight="bold" opacity="0.6" letter-spacing="3">{cat.upper()}</text>\n'

for n in nodes_data:
    x, y = node_pos[n['id']]
    svg += f'<g><rect x="{x-rect_w/2}" y="{y-rect_h/2}" width="{rect_w}" height="{rect_h}" rx="6" ry="6" fill="#ffffff" fill-opacity="0.9" stroke="{cat_colors[n["category"]]}" stroke-width="1.8"/>'
    svg += f'<text x="{x}" y="{y-1}" text-anchor="middle" font-size="12" font-family="sans-serif" font-weight="bold" fill="#2c3e50">{n["id"]}</text>'
    svg += f'<text x="{x}" y="{y+12}" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#7f8c8d">{n["year"]}</text></g>\n'

svg += '</svg>'
with open('programming_languages.svg', 'w', encoding='utf-8') as f: f.write(svg)

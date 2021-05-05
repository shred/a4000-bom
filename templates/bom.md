# Amiga 4000D Rev B - Bill Of Material

| Part ID | Qty | Part | Package | Remark | Components |
|---------|----:|------|---------|--------|------------|
{% for sec, parts in bom.items() %}{% for p in parts %}| {{ p.id }} | {{ p.quantity }} | {% if p.rare %}**{% endif %}{{ p.part }}{% if p.rare %}**{% endif %} | {{ p.package }} | {{ p.remark }} | {{ p.components|join(', ') }} |
{% endfor %}{% endfor %}

**Rare parts are bold printed.**

This list is provided "as is" and without warranties of any kind either expressed or implied.

Version: {{ version }} ({{ date }})
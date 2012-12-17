VERSION="0.1.2"
TTF_VERSION="0.1"
APPNAME='varada'
LICENSE='OFL.txt'
COPYRIGHT="Copyright SIL International, 2012"

for f in ['Regular', 'Book', 'Bold', 'Book-Bold'] :
	p = 'src/Varada-' + f
	fnt = font(target = 'Varada-' + f + '.ttf',
				source = p + '.sfd',
				license = ofl('Varada'),
				version = TTF_VERSION,
				opentype = internal(),
				graphite = gdl(p[4:] + '.gdl',
								master = 'src/varada.gdl',
								params = '-w3521'),
				ap = p + '.xml',
				script = 'lao '
			)

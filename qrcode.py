import qrcode

img = qrcode.make('https://newindiabattery-github-io.vercel.app/')
img.save('qr_code.png')
img.show()
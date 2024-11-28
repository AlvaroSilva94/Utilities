from flask import Flask, request, send_file
import io
import qrcode

app = Flask(__name__)

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    website_url = request.args.get('url')
    if not website_url:
        return 'URL parameter is missing.', 400

    # Generate the QR code image
    qr = qrcode.QRCode()
    qr.add_data(website_url)
    qr.make(fit=True)
    qr_img = qr.make_image()

    # Create an in-memory buffer to hold the image
    img_buffer = io.BytesIO()
    qr_img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # Check if the 'download' query parameter is present
    download = request.args.get('download')

    # Return the QR code image with appropriate headers based on 'download' parameter
    if download:
        return send_file(img_buffer, mimetype='image/png', as_attachment=True, attachment_filename='qr_code.png')
    else:
        return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

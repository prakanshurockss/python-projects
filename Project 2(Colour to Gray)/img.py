from PIL import Image, ImageOps

def main():

    filename = 'sample.png'
    image = Image.open( filename )
    size = width, height = image.size

    if ( image.mode == 'RGBA'):
        image.load()
        r, g, b, a = image.split( )
        image = Image.merge('RGB', (r, g, b))

    image = ImageOps.grayscale( image )

    image.save( "modified_" + filename )
    del image

if( __name__ == "__main__"):
    main()

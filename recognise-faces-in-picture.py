import face_recognition
import click
import PIL.Image

beyonce_image = face_recognition.load_image_file('beyonce.jpg')
solange_image = face_recognition.load_image_file('solange-knowles-1.jpg')

unknown_image = face_recognition.load_image_file('beyonce2.jpg')


def scan_known_people('.known./'):
    known_names = []
    known_face_encodings = []

    for file in image_files_in_folder('.known./'):
        basename = os.path.splitext(os.path.basename(file))[0]
        img = face_recognition.load_image_file(file)
        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 1:
            click.echo(
                "WARNING: More than one face found in {}. Only considering the first face.".format(file))

        if len(encodings) == 0:
            click.echo(
                "WARNING: No faces found in {}. Ignoring file.".format(file))
        else:
            known_names.append(basename)
            known_face_encodings.append(encodings[0])

    return known_names, known_face_encodings

# try:
#     beyonce_face_encoding = face_recognition.face_encodings(beyonce_image)[0]
#     solange_face_encoding = face_recognition.face_encodings(solange_image)[0]
#     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
# except IndexError:
#     print('can\'t find faces')
#     quit()


# known_faces = [
#     beyonce_face_encoding,
#     solange_face_encoding
# ]

# results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# print('Is this Beyonce?{} '.format(results[0]))
# print('Is this Solange?{} '.format(results[1]))
# print('Is this an unknown person?{}'.format(not True in results))

def print_result(filename, name, distance, show_distance=False):
    if show_distance:
        print("{},{},{}".format(filename, name, distance))
    else:
        print("{},{}".format(filename, name))


def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]

sentence = input('Please enter text: ')

if len(sentence) > 0:
    print(f'Bosh harf: {sentence[0]}, Ohirgi harf: {sentence[-1]}')
else:
    print("Matn kiritilmadi!")
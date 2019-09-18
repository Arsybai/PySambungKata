"""
GAME SAMBUNG KATA

@author : arsybai
"""
import random, requests, json, sys

start = ['a','i','u','e','o']
this_done = []
games = {
    'score':0,
    'cur':'null'
}

def newGame():
    astart = random.choice(start)
    games['cur'] = astart
    print("Dimulai dari [ {} ]".format(games['cur']))

def check(answer):
    if answer.lower().startswith(games['cur']):
        req = requests.get('https://tpxapi.herokuapp.com/kbbi?kata={}'.format(answer.lower()))
        data = json.loads(req.text)["result"][0]["arti"][0]
        if data != "tidak ditemukan":
            games['score'] += 10
            print("Score + 10")
            print(data)
            temp = "{}!".format(answer)
            dec = []
            for huruf in temp[-3:-1]:
                if huruf in start:
                    dec.append(huruf)
            if dec != []:
                games['cur'] = temp[-3:-1]
                print("\nSelanjutnya adalah [ {} ]".format(games['cur']))
            else:games['cur'] = temp[-2];print("\nSelanjutnya adalah [ {} ]".format(games['cur']))
            this_done.append(answer.lower())
        else:
            print("kata tidak ada dalam kamus!")
            games['score'] -= 5
            print("Score - 5")
            newGame()
    else:
        print("Kata salah!\nKata harus dimulai dengan [ {} ]".format(games['cur']))
        games['score'] -= 5
        print("Score -5")

def play():
    helper = """[ SELAMAT DATANG DI GAME SAMBUNG KATA ]

di game ini kalian harus nebak kata apa dengan awalan yang telah ditentukan.
jika kalian benar maka score bertambah 10.
namun jika salah maka score dikurangi 5.

silahkan ketik play untuk mulai bermain!
atau ketik help untuk menu lainnya. enjoy :)

Made by arsybai.xyz"""
    print(helper)

def menus(command):
    if command.lower() == 'help':
        print("[ HELPER ]\n> play : untuk mulai game\n> nyerah : untuk menyerah\n> score : untuk melihat score\n> exit : untuk keluar game\n\nMade by arsybai.xyz")
    elif command.lower() == 'play':
        newGame()
    elif command.lower() == 'nyerah':
        print("Ah payah kamu :(\nMulai lagi ya..")
        newGame()
    elif command.lower() == 'score':
        print("Score kamu sekarang adalah : {}".format(str(games['score'])))
    elif command.lower() == 'exit':
        sys.exit("Bye bye~\nTerimakasih sudah bermain :D\n\nScore : {}".format(str(games['score'])))
    else:
        check(command.lower()) if command.lower() not in this_done else print("Kata ini telah dijawab!")

play()
while True:
    this_ = input("> ")
    menus(this_)
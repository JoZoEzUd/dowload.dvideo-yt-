from pytubefix import YouTube #pip install pytubefix

while True:
    try:
        menu = int(input("digite (1) para abaixar um video  ou (0) para sair: "))
        if menu ==1:
            duracao= int(input("digite (2) para ver a duraçao do video ou (3) para nao ver a duraçao"))
            titulo = int(input("digite (4) para ver o titulo do video ou (3) para nao ver o titulo"))
            tamanho=int(input("digite (5) para ver o tamanho do video ou (3) para nao ver o tamanho "))
    except ValueError:
        print("digite apenas numeros (0 ou 1).")
    if menu == 1:
        link = str(input("coloque o link do video: "))
        try: 
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            print("Download concluido")
            if duracao ==2:
                print(f"duracao: {yt.length} segundos")
            if titulo == 4:
                print(f"titulo: {yt.title} ") 
            if tamanho == 5:
                print(f"tamanho do video: {yt.streams.get_highest_resolution().filesize / (1024**2):.2f}MB")
        except Exception as e:
            print("erro ao baixar:", e)
    else:
        print("saido....")
        break


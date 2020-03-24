from file import File
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
f = File()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ", 2)
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                namaFile = cstring[1].strip()
                isiFile = cstring[2].strip()
                f.uploadFile(namaFile, isiFile)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                data = {}
                data['File_List'] = []
                listFile = f.listFile()
                num = 1
                for namaFile in listFile:
                    data['File_List'].append({num: namaFile})
                    num += 1

                dict = {"Status": "Berhasil", "File": data}
                return json.dumps(dict, indent=3)
            elif (command=='download'):
                logging.warning("download")
                namaFile = cstring[1].strip()
                tmp = f.downloadFile(namaFile)
                # return json.dumps(hasil)
                return tmp
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    fm = FileMachine()
import pysftp
import ..fileread/inputfile

def setup_conn(hostname, user, pwd):

    with pysftp.Connection(host=hostname, username=user, password=pwd) as sftp:
        print("Connection succesfully stablished...REMOTE directory --> "+sftp.pwd)

        sftp.cwd('/AFS1/')
        directory_path = sftp.listdir_attr()

        for attr in directory_path:
            print(attr.filename, attr)


setup_conn('reconciliation2.milleri.it', 'sftprecon', 'R3c0nc1l1@t10n$2019')
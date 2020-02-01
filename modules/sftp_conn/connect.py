import pysftp

hostname = 'sftp'
user = 'username'
pwd = 'password'

with pysftp.Connection(host=hostname, username=user, password=pwd) as sftp:
    print("Connection succesfully stablished...REMOTE directory --> "+sftp.pwd)

    sftp.cwd('/AFS1/')
    directory_path = sftp.listdir_attr()

    for attr in directory_path:
        print(attr.filename, attr)


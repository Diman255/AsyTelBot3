import os
import shutil
import zipfile


def summ_archive():
    path = ' save'
    print(os.path.isdir(path))
    if os.path.isdir(path):
        file_sum_size = 0
        i = 0
        n = 0
        archiv_id = []
        result_archiv_id = ['Архив фото и видео']
        text = 'None'
        zipf = zipfile.ZipFile("archive/myzipfile.zip", "w")
        zipf1 = zipfile.ZipFile("archive/myzipfile1.zip", "w")
        zipf2 = zipfile.ZipFile("archive/myzipfile2.zip", "w")
        zipf3 = zipfile.ZipFile("archive/myzipfile3.zip", "w")
        zipf4 = zipfile.ZipFile("archive/myzipfile3.zip", "w")
        zipf5 = zipfile.ZipFile("archive/myzipfile3.zip", "w")

        for dirs, folder, files in os.walk(path):
            for file in files:
                file_name = os.path.join(dirs, file)
                file_size = os.path.getsize(file_name)
                file_sum_size = file_sum_size + file_size
                if file_size < 48 * 1024 * 1024:

                    if file_sum_size < 48 * 1024 * 1024:
                        i = 0
                        zipf.write(file_name, os.path.relpath(file_name, os.path.join(path, '.')))
                    elif 48 * 1024 * 1024 <= file_sum_size < 98 * 1024 * 1024:
                        i = 1
                        zipf1.write(file_name, os.path.relpath(file_name, os.path.join(path, '.')))
                    elif 98 * 1024 * 1024 <= file_sum_size < 148 * 1024 * 1024:
                        i = 2
                        zipf2.write(file_name, os.path.relpath(file_name, os.path.join(path, '.')))
                    elif 148 * 1024 * 1024 <= file_sum_size < 198 * 1024 * 1024:
                        i = 3
                        zipf3.write(file_name, os.path.relpath(file_name, os.path.join(path, '.')))
                    elif 198 * 1024 * 1024 <= file_sum_size < 248 * 1024 * 1024:
                        i = 4
                        zipf4.write(file_name, os.path.relpath(file_name, os.path.join(path, '.')))
                    elif 248 * 1024 * 1024 <= file_sum_size < 298 * 1024 * 1024:
                        i = 5
                        zipf5.write(file_name, os.path.relpath(file_name, os.path.join(path, '.')))
                else:
                    text = 'Пропущен файл более 50 Мб'
        zipf.close()
        zipf1.close()
        zipf2.close()
        zipf3.close()
        zipf4.close()
        zipf5.close()

        file_id1 = r'archive/myzipfile.zip'
        file_id11 = r"archive/myzipfile1.zip"
        file_id12 = r"archive/myzipfile2.zip"
        file_id13 = r"archive/myzipfile3.zip"
        file_id14 = r"archive/myzipfile4.zip"
        file_id15 = r"archive/myzipfile5.zip"

        result_archiv = [file_id1, file_id11, file_id12, file_id13, file_id14, file_id15]

        for n in range(i + 1):
            archiv_id.append(result_archiv[n])

        result_archiv_id.append(text)
        result_archiv_id.append(archiv_id)

        print(i)
        print(file_sum_size / (1024 * 1024))
        print()

        shutil.rmtree(path)
        return result_archiv_id
    else:
        result_archiv_id = ['Обновления архива фото и видео - нет']
        return result_archiv_id






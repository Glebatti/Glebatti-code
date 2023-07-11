Для создания общей папки (shared) для обмена файлами и т.д. между виртуальной машиной (далее - VM) и рабочим компьютером выполнить последовательность действий:
1. В окне Oracle VM VirtualBox Manager выбрать необходимую виртуальную машину и нажать кнопку Settings (Ctrl + S).
2. В открывшимся окне <название VM> - Settings в панели навигации выбрать Shared Folders. В основной области окна будет показан менеджер общих папок, с помощью которого можно создавать, настраивать и удалять общие папки VM.
3. Нажать кнопку Adds new shared folder. В открывшимся окне Add Share в поле Folder Path указать путь к общей папке на рабочем компьютере.
4. В поле Folder Name указать имя общей папки, которое будет отображаться в файловой системе VM.
5. По необходимости утановить свойства папкии: Read-only - только для чтения; Auto-mount - автоматически монтировать папку при загрузке операционной системы; Mount point - точка монтирования общей папки к файловой системе VM.
6. Проверить заданные настройки и нажать OK.
Настройки для проекта tgen:
1. Folder Path - C:\avs
2. Folder Name - Shared
3. Auto-mount - checked
4. Mount point - /

Для отображения меню виртуальной нашины (Mini ToolBar) сверху экранной области, выполнить действия:
1. В окне Oracle VM VirtualBox Manager выбрать необходимую виртуальную машину и нажать кнопку Settings (Ctrl + S).
2. В открывшимся окне <название VM> - Settings в панели навигации выбрать User Interface. В основной области окна поставить галочку в поле Show at Top of Screen.
3. Проверить заданные настройки и нажать OK.
Настройки для проекта tgen:
Show at Top of Screen - checked

Для установки системы управления версиями Git выполнить действия:
1. Запустить приложение Git-<версия>-64-bit из директории ./distr.
2. При запросе указания директории установки (Select Destination Location) - оставить значение пути по умолчанию.
3. На этапе выбора компонентов (Select Components) отметить пункт (NEW!) Add a Git Bash Profile to Windows Terminal.
4. При выборе редактора по умолчанию (Choosing the default editor used by Git) - в
комбобоксе выбрать значение Use Notepad++ as Git's default editor.
5. При конфигурировании способа обработки окончания строк (Configuring the line ending conversions) выбрать значение Checkout as-is, commit as-is.
6. Остальные параметры следует оставить по умолчанию.
7. Закрыть окно установки.
8. Перейти к расположению ярлыка Git Bash и в свойствах в поле Быстрый вызов (Shortcut) указать комбинацию клавиш Ctrl + Alt + T
9. Нажать комбинацию клавиш Ctrl + Alt + T - откроется окно терминала (далее - открыть терминал). В терминале набрать команду git --version. При успешной установке будет выведена версия установленной системы управления версиями.
10. Пpи необходимости настроить внешний вид терминала - ПКМ на заголовке окна терминала, выбрать пункт Options. В разделе Looks и Text выбрать требуемые настройки внешнего вида.

Примечание:
Вставить в терминал значение из буфера обмена - Shift + Insert.


Настройки для проекта tgen:
1. Выполнить Git-2.37.1-64-bit.exe
2. Настроить Git, подав команды:
	git config --global user.email "kovalevsa@mail.ru"
	git config --global user.name "KovalevSA"

Установка Python версии 3.10:
1. В консоли выдать команду
	python-<версия>-amd64.exe /quiet /passive InstallAllUsers=1 PrependPath=1
2. Переоткрыть консоль. Проверить успешность установки Python командой
	py --version
3. Проверить наличие пути до интерпретатора python.exe в переменных окружения (Environment variables) подачей команды:
	echo %PATH%
	В выводе пронтролировать наличие пути до интерпретатора python, например: "C:\Program Files\Python310\Scripts\;C:\Program Files\Python310\...";
	В случае отсутствия пути, добавить его командой:
	set PATH=C:\Program Files\Python310\Scripts\;C:\Program Files\Python310\;%PATH%

Установка пакетов python при помощи утилиты pip:
1. Убедиться, что менеджер пакетов pip доступен в системе с помощью команды, поданной в терминале:
	pip --version
	Вывод команды должен быть похож на следующее:
	pip X.Y.Z from C:\Program Files\Python310\lib\site-packages\pip (python 3.N.N)
2. Перейти в директорию, содержащую пакеты, например:  cd /c/avs/distr/Python3.10/
3. Убедиться, что файлы находятся в указанной дирректории командой:
	ls -la
4. Установить нужный пакет командой:
	pip install <имя пакета>
	Пример: pip install Jinja2-3.1.2-py3-none-any.whl
	Контролировать вывод на наличие строки: Successfully installed <имя пакета>, означающую успешную установку пакета.
5. Проконтролировать, что все пакеты были установлены с помощью команды:
	pip list

Настройки для проекта tgen:
1. pip install peewee-3.15.1.tar.gz
2. pip install MarkupSafe-2.1.1-cp310-cp310-win_amd64.whl
3. pip install Jinja2-3.1.2-py3-none-any.whl

Установка Visual Studio Code (VSC):
1. В консоли выполнить команду:
	VSCodeUserSetup-x64-1.69.2.exe /silent /mergetasks='!runcode,addcontextmenufiles,addcontextmenufolders,associatewithfiles,addtopath'
2. Переоткрыть консоль. Проверить успешность установки VSC командой:
	code --version

Настройка терминала Bash по умолчанию:
1. Открыть командную строку VSC нажав комбинацию клавиш Ctrl + Shift + P. Затем ввести "open user settings" и выбрать предложенный пункт из выпадающего меню "Open User Settings"
2. В строке поиска (Search string) ввести путь "terminal.integrated.shell.windows".
3. В предложенном VSC комбо-боксе выбрать значение Git Bash.

Установка расширений (extension) для VSC:
1. Запустить VSC подав команду в терминале:
	code &
	Примечание: & - запуск программы в фоновом режиме (таким образом программа не зависит от терминала)
2. В VSC активировать терминал (Ctrl + `). В терминале VSC перейти в директорию с расширениями и выполнить установку с помощью команды:
	code --install-extension <имя пакета>
3. Контролировать установку пакета можно в боковой вкладке VSC Extensions (Ctrl+ Shift + X).

Настройки для проекта tgen:
1. code --install-extension ms-python.python-2022.11.12071744.vsix
2. code --install-extension DotJoshJohnson.xml-2.5.1.vsix
3. code --install-extension James-Yu.latex-workshop-8.28.0.vsix

Выбор директории для работы в VSC:
1. В VSC открыть папку с файлами для работы (Ctrl + O) и выбрать путь до папки с необходимыми файлами.

Настройки для проекта tgen:
1. C:\avs\source\tgen

Установка MiKTeX и TexStudio:
1. Распаковать архив ProTeXt-3.1.9-121317 в текущую директорию (.\ProTeXt). Нажать кнопку Extract.
2. Запустить инструмент Protext, исполнением файла Setup.exe.
P.S. Если на компьютере уже установлена другая версия MiKTeX или другой дистрибутив Latex, то они должны быть предварительно удалены с компьютера.
3. В открывшимся окне нажать кнопку "Install" напротив "MiKTeX" для установки MiKTeX.
4. При установке MiKTeX следовать рекомендациям программы установки. Выбрать тип установки "Complete MiKTeX"
5. Задать настройки: "Install MiKTeX for:" - "Anyone who uses this computer (all users)", "Preferred paper" - "A4", "Install missing paskages on-the-fly" - "Yes"
6. В окне "proTeXt" нажать кнопку "Install" напротив "TeXStudio" для установки TeXStudio. При установке TeXStudio следовать рекомендациям программы установки.
7. После установки нажать кнопку "Enter" в окне "proTeXt"

Настройка MiKTeX и TexStudio:
1. Для установки словарей разархивировать "russian_english.zip" командой 
	unzip russian_english.zip
2. Создать директорию в случае ее отсутствия командой
	mkdir "/c/Program Files (x86)/TeXstudio/dictionaries"
3. Cкопировать файлы словарей ("russian_english.aff", "russian_english.dic") в каталог с установленным TeXstudio (по умолчанию "C:\Program Files (x86)\TeXstudio\dictionaries") командой
	cp russian_english.aff russian_english.dic /c/Program\ Files\ \(x86\)/TeXstudio/dictionaries/
4. Удалить распакованные файлы командой
	rm russian_english.dic russian_english.aff
5. Установить дополнительные словари в соответствии с инструкцией "Initial_Setup.pdf" 8 Глава (стр. 24) пункты 8.12 - 8.13.
6. Для поддержки шрифта Times New Roman установить пакет PSCyr, согласно инструкции "Setup_PSCyr.pdf", но с учётом того, что архив "PSCyr.zip" находится в корне этого каталога.

Замена старых файлов на новые (доработанные):
1. Скопировать содержимое папки (из архива Generator)"Template_generator\For DWNT From XML" в рабочую папку с проектом "Utilities\Template_generator\For DWNT From XML"

Настройки для проекта tgen:
1. "C:\avs\Utilities\".

2. Скопировать содержимое папки (из архива Generator) "Reports" в папку "Racks\DWNT\docs\Reports".

Настройки для проекта tgen:
1. "C:\avs\Racks\DWNT\docs\Reports".

Компиляция TeXStudio:
1. Настроить программу TeXStudio в соответствии с инструкцией "TemplateInstruction".

Настройка NI Stand для корректного отображения XML-файла в Internet explorer.

Для открытия XML файла в его исходном виде можно использовать программу Notepad++.
Файл "<название файла-отчета>.xml" является исходным файлом XML, который шаблонизатор преобразует в PDF файл "<выходное название файла>.pdf".

Для открытия XML файла в "Internet Explorer" в красивом виде таблицы необходим файл стилей TestStand. 

Если программа TestStand не установлена на компьютер, то для открытия XML файла в "Internet Explorer" можно в файле "Template_generator\For DWNT From XML\Main_20GK-01_Report[10 15 53][03.03.2022]_62097207.xml" в самой первой строке (при его открытии через Notepad++) найти атрибут "href". Там будет указан стандартный путь, где xml пытается найти файлы, что бы красиво отобразиться в Internet explorer 

Скопировать файлы из NI TestStand StyleSheets в указанные директории. В случае, если директорий нет - создать вручную по указанным путям
1. "C:\Program Files\National Instruments\TestStand 2017\Components\Models\TestStandModels\ATML\StyleSheets"
2. "C:\Program Files x86\National Instruments\TestStand 2017\Components\Models\TestStandModels\ATML\StyleSheets"
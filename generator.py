import os


def border_decorator(func):
    def wrapper(*args, **kwargs):
        print("================================== \n")
        func(*args, **kwargs)
        print("\n==================================")

    return wrapper


class CodeGenerator:
    def __init__(self):
        self.initial_path: str = "/home/azamat/Developer/Django"
        self.start_type: int = 0
        self.project_path: str = self.initial_path

    def validate_start_type(self, start_type):
        try:
            if start_type in ("1", "2"):
                self.start_type = int(start_type)
            else:
                raise ValueError()
        except ValueError:
            print("Введите 1 или 2")

    def choose_start_type(self):
        while not self.start_type:
            start_type = input("Выберите тип настройки: \n 1.Новый проект \n 2.Существующий проект \n Ввод: ")
            self.validate_start_type(start_type)

    def generate_project_by_type(self):
        if self.start_type == 1:
            self.generate_new_project()
        else:
            self.modify_existing_project()

    @border_decorator
    def generate_new_project(self):
        pass

    def modify_existing_project(self):
        """ TODO: Сделать модификацию созданного проекта """
        project_index = 0

        print("Выберите директорию проекта: ")

        while True:
            print("================================== \n")

            initial_dirs_list = os.listdir(self.project_path)

            for index, path_file in enumerate(initial_dirs_list):
                print(f"{index}.{path_file}")
            print("================================== \n")

            while True:
                try:
                    project_index = int(input("Введите номер директории: "))
                    project_path = initial_dirs_list[project_index]
                    break
                except IndexError:
                    print(f"Проект под номером {project_index} не существует. Попробуйте еще раз")
                except ValueError:
                    print(f"Введите номер от 0 до {len(initial_dirs_list)}")

            if "manage.py" not in os.listdir(f"{self.project_path}/{project_path}"):
                self.project_path += f"/{project_path}"
            else:
                print(self.project_path)
                break
            DatabaseManager(self.project_path)

    def start(self):
        self.choose_start_type()
        self.generate_project_by_type()


class DatabaseManager:
    def __init__(self, project_path):
        self.project_path = project_path
        self.settings_location = self.get_settings_location()

    def get_settings_location(self):
        print(self.project_path)
        return "Hello"

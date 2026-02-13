import ast



class load:

    @staticmethod
    def read() -> None:
        """
        Reads the save file
        Retuns
        -------

        """
        try:
            with open("save_load/savefile.txt", "r") as file:
                content = file.readline().split("|")
                resources = content[0].strip("[]").split(",")
                #prompt ganzes file
                #chatgpt anfang
                inv = ast.literal_eval(content[1].strip())
                Map_R = ast.literal_eval(content[2].strip())
                Map_C = ast.literal_eval(content[3].strip())
                # ende
            return True, resources, inv, Map_R, Map_C
        except:
            return False, 0, 0, 0, 0


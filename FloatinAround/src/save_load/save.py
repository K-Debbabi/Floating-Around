


class save():

    @staticmethod
    def store(resources, inv, mapR, mapC):
        """
        Speichert das Gameplay so gut wie möglich

        Parameters
        ----------
        resources alle resourcen
        inv inventar
        mapR raft map
        mapC campfire map
        """
        with open("save_load/savefile.txt", "w") as file:
            file.write(f"{resources}|")
            file.write(f"{inv}|")
            file.write(f"{mapR}|")
            file.write(f"{mapC}|")
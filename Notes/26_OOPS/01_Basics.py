import time

# Self Defined exceptions

class NotDeployed(Exception):
    pass

class DeploymentError(Exception):
    pass

class AlreadyDeployedError(Exception):
    pass

class EmptyHist(Exception):
    pass


class ModelDeployment:
    def __init__(self, m_name, ver):
        self.m_name = m_name
        self.ver = ver
        self.deployed = False
        self.d_time = None
        self.hist = list()

    def deploy(self):

        if self.deployed:
            raise AlreadyDeployedError(
                f"Model {self.m_name} v{self.ver} is already deployed \n If you think this is an error report responsible team"
            )

        self.d_time = time.ctime()

        self.deployed = True

        print("\n=============================== Deploy Info =========================")
        print(f"Deploying {self.m_name}")
        print(f"Version : {self.ver}")
        print(f"Deploy Time : {self.d_time}")
        print("\n")

        self.hist.append(f"Deployed model {self.m_name} v{self.ver} at {self.d_time}")


    def rollback(self, ver: str):
        if not self.deployed:
            raise NotDeployed(
                f"The Model is not deployed"
            )

        if self.ver == ver:
            raise AlreadyDeployedError(
                f"Cannot Rollback to the same version \n Current verion : {self.ver} \n Reffered Version : {ver} \n If you think this is an error report responsible team"
            )

        prev_ver = self.ver
        self.ver = ver
        self.d_time = time.ctime()


        print("=============================== Roll Back info =========================")
        print(f"Rollback to from version {prev_ver} to version {ver} successful")
        print("\n")

        self.hist.append(f"Rolled backed v{prev_ver} to v{ver}")


    def status(self):
        print("\n =============================== Status =========================")
        print(f"Model Name : {self.m_name}")
        print(f"Model Version : {self.ver}")
        print(f"Deployed : {self.deployed}")
        if self.deployed:
            print(f"Deploy Time : {self.d_time}")
        print("\n")

    def recall(self):
        print("=============================== Recall info =========================")
        if not self.deployed:
            raise NotDeployed(
                f"The Model is not deployed"
            )

        self.deployed = False
        print(f"Recall of {self.m_name} version {self.ver} Successful")

        self.hist.append(f"Recalled {self.m_name} version {self.ver}")

    def gethist(self) -> None:
        if not self.hist:
            raise EmptyHist(
                f"The History is empty. Nothing has been done \n If you think this is an error report responsible team"
            )

        print(f"============================= HISTORY ====================================")
        i = 1
        for ele in self.hist:
            print(f"{i}: {ele}")
            i += 1




def main() -> None:
    kox = ModelDeployment("kox", "2.1")
    kox.deploy()
    kox.gethist()

if __name__ == "__main__":
    main()

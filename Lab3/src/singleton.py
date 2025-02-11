class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        # Check if the class has an instance. If not call the constructor
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init_singleton()
        else:
            print(f"logger already created")
            print(f"Memory location: {id(cls._instance)} \n")

        return cls._instance
    
    def init_singleton(self):
        print(f"Logger created exactly once")
        print(f"Memory location: {id(self)} \n")

        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()

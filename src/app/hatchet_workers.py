from workers.hatchet_worker import upload_image_worker
def main():
    upload_image_worker.start()

if __name__ == "__main__":
    main()
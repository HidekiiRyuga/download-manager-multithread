class ChunkManager:

    def __init__(self, file_size, num_chunks):

        self.file_size = file_size
        self.num_chunks = num_chunks

    def create_chunks(self):

        chunk_size = self.file_size // self.num_chunks

        chunks = []

        start = 0

        for i in range(self.num_chunks):

            end = start + chunk_size - 1

            if i == self.num_chunks - 1:
                end = self.file_size - 1

            chunks.append((start, end))

            start = end + 1

        return chunks
import os


class FileAssembler:

    def assemble(self, output_filename, num_chunks):

        with open(output_filename, "wb") as output_file:

            for i in range(num_chunks):

                chunk_name = f"chunk_{i}.part"

                with open(chunk_name, "rb") as chunk_file:

                    output_file.write(
                        chunk_file.read()
                    )

        print(
            f"Assembled: {output_filename}"
        )

        for i in range(num_chunks):

            chunk_name = f"chunk_{i}.part"

            os.remove(chunk_name)

        print(
            "Temporary chunk files deleted"
        )
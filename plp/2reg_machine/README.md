2Reg Machine
============

## Usage

#### Docker (recommended)
In root folder execute
```bash
docker build . -t <container_tag>
docker run -it <container_tag> sh
python3 . '<file_path>'
```
<file_path> is the file will be read, default is 2r_program.txt  
<container_tag> is the name container will be

#### Python
In code folder execute
```python
python3 .
```
or
```python
python3 . '<file_path>'
```
<file_path> is the file will be read, default is 2r_program.txt

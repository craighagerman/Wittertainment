
Direct SSH 
```bash
ssh -p 40173 root@50.20.127.188 -L 8080:localhost:8080
```

scp to transfer jupyter notebook
```bash
scp -P 40173 src/notebooks/vast/diarize.ipynb root@50.20.127.188:/workspace/
```

scp to copy transcipts to local machine

```bash

scp -r -P 40173 root@50.20.127.188:/workspace/transcripts ~/Data/
```


# random-choice-yojijukugo
Randomly select one yojijukugo (four-character idiom)

<details><summary>random_choice_yojijukugo.mp4</summary>

<video controls src="https://github.com/user-attachments/assets/baf60d72-6eb4-482c-b971-79a7f70f0d37" muted="false"></video>

</details>

## flask + vue3

### flask

```bash
cp -p .env.example .env
```

```bash
pipenv shell
```

```bash
pipenv install --dev
```

```bash
python app.py
```

#### redis

```bash
docker-compose up -d
```

### vue3

```bash
cd client/
```

```bash
npm i
```

```bash
npm run serve
```

Open http://localhost:8080/

## When using production build

### flask

```bash
echo "USE_FLASK_CORS=false" > .env
```

```bash
python app.py
```

#### redis

```bash
docker-compose up -d
```

Open http://127.0.0.1:5000

### vue3

Update production build

```bash
cd client/
```

```bash
npm run build
```

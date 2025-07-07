## 上傳映像檔到 Google Artifact Registry (GAR)

要將映像檔上傳到 Google Artifact Registry (GAR)，你需要稍微更改一些設定。以下是修改後的語法，假設你使用的是 Artifact Registry 位於某個區域的存儲庫。

### 假設：
- 你有 `gcp_json` 變數，其中包含了 GCP JSON 金鑰。
- 你想上傳到位於 `asia` 區域的 Artifact Registry。

### 修改後的命令：
```bash
echo $gcp_json | docker login -u _json_key --password-stdin https://asia-east1-docker.pkg.dev
```

### 其他步驟：
#### 替換 GCR URL 為 GAR URL:
- 在 GCR (Google Container Registry)，你會看到類似 `gcr.io` 的 URL。
- 在 GAR (Google Artifact Registry)，URL 的格式是 `REGION-docker.pkg.dev`，例如 `asia-east1-docker.pkg.dev`。

#### 指定 Artifact Registry 的專案和存儲庫名稱:
你需要確保 docker 註冊的是正確的 Artifact Registry 存儲庫。例如，如果你的存儲庫是 `$REPOSITORY_NAME`，專案是 `$PROJECT_ID`，並且該存儲庫位於亞洲區域，那麼推送命令應該是：

```bash
docker tag $IMAGE_NAME asia-east1-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE_NAME
docker push asia-east1-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE_NAME
```

### 完整流程：
#### 設定認證：
```bash
echo $gcp_json | docker login -u _json_key --password-stdin https://asia-east1-docker.pkg.dev
```

#### 標籤 Docker 映像檔：
假設你已經有一個本地映像檔 `$IMAGE_NAME`，你需要先標籤它為 Artifact Registry 的目標存儲庫。

```bash
docker tag $IMAGE_NAME asia-east1-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE_NAME:latest
```

#### 上傳到 Artifact Registry：
最後，將映像檔推送到 GAR。

```bash
docker push asia-east1-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE_NAME:latest
```

這樣就完成了從 Docker 將映像上傳到 Google Artifact Registry 的流程。
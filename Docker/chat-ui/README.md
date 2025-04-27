File **.env.local** trong dự án Chat UI của Hugging Face là nơi bạn ghi đè (override) các biến môi trường mặc định được định nghĩa trong file **.env**. Đây là tập tin quan trọng để cấu hình các thông số cần thiết cho ứng dụng chạy đúng cách trên môi trường cục bộ (local) hoặc cho mục đích thử nghiệm. Dưới đây là các nhóm cấu hình chính cùng với ý nghĩa của chúng:

---

### 1. Cấu hình Cơ sở Dữ liệu (Database)

- **MONGODB_URL**  
  Đây là URL kết nối đến instance MongoDB, nơi lưu trữ lịch sử trò chuyện. Ví dụ:  
  `MONGODB_URL=mongodb://localhost:27017`  
  Nếu bạn dùng Docker, có thể chạy MongoDB với lệnh như:  
  ```bash
  docker run -d -p 27017:27017 --name mongo-chatui mongo:latest
  ```  
  citeturn0search0

- **MONGODB_DB_NAME**  
  Tên cơ sở dữ liệu sẽ được sử dụng (ví dụ: `chat-ui`).

- **MONGODB_DIRECT_CONNECTION**  
  Giá trị Boolean (true/false) cho biết có sử dụng kết nối trực tiếp đến MongoDB hay không.

---

### 2. Cấu hình Token và API Keys

- **HF_TOKEN**  
  Token truy cập của Hugging Face dùng để xác thực các yêu cầu tới API của Hugging Face (bao gồm truy xuất mô hình, tokenizer, v.v.). Bạn có thể lấy token này tại [Hugging Face settings](https://huggingface.co/settings/token).  
  citeturn0search0

- **OPENAI_API_KEY, ANTHROPIC_API_KEY, CLOUDFLARE_API_TOKEN, COHERE_API_TOKEN, GOOGLE_GENAI_API_KEY, …**  
  Đây là các khóa API dành cho các nhà cung cấp dịch vụ mô hình bên ngoài (OpenAI, Anthropic, Cloudflare, Cohere, Google, v.v.) giúp Chat UI có thể gọi đến các endpoint inference khác nhau.

---

### 3. Cấu hình Mô hình (Models)

- **MODELS**  
  Biến này chứa một mảng (trong dạng JSON string) mô tả các mô hình có sẵn cho ứng dụng. Mỗi đối tượng trong mảng định nghĩa:  
  - **name**: Tên hoặc ID của mô hình.  
  - **displayName**: Tên hiển thị (nếu có).  
  - **description**: Mô tả ngắn gọn về mô hình.  
  - **promptExamples**: Danh sách các ví dụ prompt giúp người dùng hiểu cách tương tác với mô hình.  
  - **parameters**: Các thông số như `temperature`, `top_p`, `max_new_tokens`,… để điều chỉnh cách mô hình sinh ra phản hồi.  
  - **endpoints**: Thông tin cấu hình endpoint (ví dụ: loại endpoint như “llamacpp”, “openai”, “tgi”, URL endpoint,…) để ứng dụng biết cách kết nối và truy vấn mô hình.  
  citeturn0search1

- **OLD_MODELS**  
  Dùng để lưu trữ các cấu hình mô hình đã bị loại bỏ (giúp cho việc chuyển đổi hoặc lưu trữ lịch sử cấu hình).

- **TEXT_EMBEDDING_MODELS**  
  Định nghĩa các mô hình nhúng (embedding) được sử dụng trong chức năng web search. Mỗi mô hình có các thuộc tính như `name`, `chunkCharLength` và `endpoints`. Mặc định, Chat UI sử dụng mô hình Xenova/gte-small cho tác vụ nhúng văn bản.  
  citeturn0search1

---

### 4. Cấu hình Xác Thực và Đăng Nhập

- **OPENID_CONFIG**  
  Cấu hình OpenID Connect để kích hoạt tính năng đăng nhập qua nhà cung cấp OIDC (ví dụ: Google, Hugging Face). Thông tin gồm URL của issuer, CLIENT_ID, CLIENT_SECRET, và phạm vi (scopes).  
  citeturn0search2

- **MESSAGES_BEFORE_LOGIN**  
  Số lượng tin nhắn người dùng có thể gửi trước khi bắt buộc đăng nhập.

- **ALLOWED_USER_EMAILS, ALLOWED_USER_DOMAINS, ALTERNATIVE_REDIRECT_URLS**  
  Các biến này kiểm soát danh sách người dùng hoặc miền email được phép đăng nhập, cũng như cấu hình redirect URL cho OAuth.

---

### 5. Cấu hình Cookies

- **COOKIE_NAME**  
  Tên của cookie được sử dụng để lưu trữ phiên (session) của người dùng.

- **COOKIE_SAMESITE** và **COOKIE_SECURE**  
  Các thuộc tính bảo mật cho cookie, cho biết cookie có chỉ gửi qua HTTPS hay có giới hạn gửi cho cùng một trang gốc (SameSite) hay không.

---

### 6. Cấu hình Web Search

Nếu bạn muốn sử dụng tính năng tìm kiếm trên web, các biến dưới đây cần được định nghĩa:

- **SERPAPI_KEY, SERPER_API_KEY, YDC_API_KEY, SERPSTACK_API_KEY, SEARCHAPI_KEY**  
  Các khóa API của các dịch vụ tìm kiếm khác nhau (SERP API, serper.dev, docs.you.com, v.v).

- **USE_LOCAL_WEBSEARCH**  
  Đặt giá trị `true` để sử dụng chế độ tìm kiếm cục bộ (local websearch) thay vì gọi API bên ngoài.

- **SEARXNG_QUERY_URL**  
  URL truy vấn của SearXNG, nơi ký tự `<query>` sẽ được thay thế bằng từ khóa tìm kiếm.

- **WEBSEARCH_JAVASCRIPT**  
  Cho phép chạy JavaScript khi phân tích trang web, giúp cải thiện khả năng tương thích (với chi phí sử dụng CPU cao hơn).

- **WEBSEARCH_TIMEOUT**  
  Thời gian chờ (tính bằng mili giây) trước khi timeout khi tải trang web.

- **ENABLE_LOCAL_FETCH**  
  Cho phép truy cập đến mạng nội bộ (local network fetch) nếu được cấu hình đúng các quy tắc bảo mật.

  citeturn0search3

---

### 7. Cấu hình Giao Diện Ứng Dụng Công Khai (Public App Configuration)

- **PUBLIC_APP_NAME, PUBLIC_APP_ASSETS, PUBLIC_APP_COLOR, PUBLIC_APP_DESCRIPTION**  
  Các biến này định nghĩa tên, màu sắc, biểu tượng và mô tả của ứng dụng công khai.

- **PUBLIC_APP_DATA_SHARING**  
  Cho phép người dùng bật/tắt tùy chọn chia sẻ dữ liệu cuộc trò chuyện với tác giả mô hình.

- **PUBLIC_APP_DISCLAIMER, PUBLIC_APP_DISCLAIMER_MESSAGE**  
  Các thông điệp cảnh báo hoặc tuyên bố từ chối trách nhiệm hiển thị trên trang đăng nhập.

- **PUBLIC_ANNOUNCEMENT_BANNERS**  
  Cấu hình các banner thông báo công khai (ví dụ: thông báo mở mã nguồn trên GitHub).

- **PUBLIC_ORIGIN, PUBLIC_SHARE_PREFIX**  
  Xác định URL gốc của ứng dụng và tiền tố URL dùng khi chia sẻ cuộc trò chuyện.

- **PUBLIC_GOOGLE_ANALYTICS_ID, PUBLIC_PLAUSIBLE_SCRIPT_URL, PUBLIC_APPLE_APP_ID**  
  Các biến dành cho tích hợp công cụ phân tích và theo dõi (nếu cần).

  citeturn0search2

---

### 8. Cấu hình Tính Năng (Feature Flags) và Giới Hạn Sử Dụng (Rate Limits)

- **LLM_SUMMARIZATION**  
  Bật chức năng tóm tắt cuộc trò chuyện bằng mô hình ngôn ngữ (LLM).

- **ENABLE_ASSISTANTS, ENABLE_ASSISTANTS_RAG, REQUIRE_FEATURED_ASSISTANTS, COMMUNITY_TOOLS**  
  Các cờ bật/tắt các tính năng phụ trợ như trợ lý ảo, tính năng tìm kiếm kết hợp (RAG) và công cụ cộng đồng.

- **EXPOSE_API, ALLOW_IFRAME**  
  Quy định việc cho phép truy cập API của ứng dụng và cho phép nhúng trang web trong iframe.

- **USAGE_LIMITS**  
  Cấu hình giới hạn về số lượng cuộc trò chuyện, tin nhắn, độ dài tin nhắn, số tin nhắn mỗi phút, v.v.

- **HF_ORG_ADMIN, HF_ORG_EARLY_ACCESS**  
  Các cờ dành cho quản trị viên hoặc người dùng có quyền truy cập sớm.

- **WEBHOOK_URL_REPORT_ASSISTANT**  
  URL webhook để nhận thông báo về báo cáo hoặc yêu cầu tính năng.

- **METRICS_ENABLED, METRICS_PORT, LOG_LEVEL**  
  Cấu hình theo dõi hiệu năng và mức độ log của ứng dụng.

- **PARQUET_EXPORT_DATASET, PARQUET_EXPORT_HF_TOKEN, ADMIN_API_SECRET**  
  Các biến cấu hình dùng cho xuất dữ liệu (Parquet export) và xác thực API của quản trị viên.

- **Các biến xây dựng Docker**:  
  Như **APP_BASE** (đường dẫn cơ sở của ứng dụng) và **PUBLIC_APP_COLOR** (màu chủ đạo) được truyền vào lúc build Docker.

- **BODY_SIZE_LIMIT**  
  Giới hạn kích thước body của yêu cầu (đặc biệt với SvelteKit).

- **Các biến Legacy**:  
  Như **HF_ACCESS_TOKEN** (khuyến cáo dùng HF_TOKEN thay thế), **ALLOW_INSECURE_COOKIES**, **PARQUET_EXPORT_SECRET**, **RATE_LIMIT**.

- **Các biến liên quan đến OpenID**:  
  Bao gồm **OPENID_CLIENT_ID**, **OPENID_CLIENT_SECRET**, **OPENID_SCOPES**, **OPENID_NAME_CLAIM**, **OPENID_PROVIDER_URL**, **OPENID_TOLERANCE**, **OPENID_RESOURCE**.

  citeturn0search1

---

### Tổng Kết

File **.env.local** của Chat UI chứa rất nhiều cấu hình cần thiết để:

- Kết nối với cơ sở dữ liệu (MongoDB).
- Xác thực và truy cập các dịch vụ bên ngoài (Hugging Face, OpenAI, Anthropic, …).
- Cấu hình các mô hình (bao gồm cả cấu hình endpoints, các tham số cho mô hình, template prompt, …).
- Điều chỉnh giao diện và các tính năng công khai của ứng dụng.
- Cấu hình các tính năng bảo mật, xác thực và giới hạn sử dụng.

Thông qua việc điều chỉnh các biến môi trường trong **.env.local**, bạn có thể tùy biến Chat UI theo nhu cầu của mình và đảm bảo ứng dụng hoạt động đúng cách trong môi trường phát triển hoặc sản xuất.

Các tài liệu và ví dụ cấu hình chi tiết có thể tham khảo trong [tài liệu của Chat UI trên Hugging Face](https://huggingface.co/docs/chat-ui/en/installation/local) và [trên GitHub của dự án Chat UI](https://github.com/huggingface/chat-ui/blob/main/.env).  
citeturn0search0 citeturn0search1

---

Với cấu hình trong **.env.local**, bạn có thể nhanh chóng thiết lập và chạy thử Chat UI cục bộ, điều chỉnh theo nhu cầu riêng về mô hình, giao diện và tích hợp các dịch vụ API bên ngoài.


# fib_api

本プロジェクトは、指定された `n` 番目のフィボナッチ数を返すREST APIである。
FastAPIを用いて実装しており、簡潔かつ保守性の高い構成とした。

## プロジェクト概要

- 正の整数 `n` を受け取り、n番目のフィボナッチ数を返す
- FastAPIによるAPI設計および、型制約による入力バリデーションを導入
- pytestを用いたユニットテストを実装済み
- Renderを用いて外部公開し、実際にHTTPリクエストを送信可能な環境を構築済み

## 公開URL

- ベースURL: https://fib-api-qg2r.onrender.com
- APIエンドポイント: `/fib?n=<整数>`

### 例：
https://fib-api-qg2r.onrender.com/fib?n=20  
→ `{ "result": 6765 }`

- ドキュメント: https://fib-api-qg2r.onrender.com/docs


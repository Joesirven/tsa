export class FetchWrapper {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    async get(endpoint, options = {}) {
        try {

            const response = await fetch(this.baseURL + endpoint, options)
            const data = await response.json()
            console.log("this is data:", data)
            if (response.ok) {
                const data = await response.json()
                return data
            } else {
                console.log(response)
                throw new Error('Response not "OK"')
            }
        } catch (error) {
            console.error('error', error)
        }
    }

    async put(endpoint, body) {
        return this._send("PUT", endpoint, body)
    }

    async post(endpoint, body) {
        return this._send("POST", endpoint, body)
    }

    async delete(endpoint, body) {
        return this._send("DELETE", endpoint, body)
    }

    async _send(method, endpoint, body) {
        try {
            const response = await fetch(this.baseURL + endpoint, {
                method: method,
                body: JSON.stringify(body),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            if (response.ok) {
                const data = await response.json()
                return data
            } else {
                throw new Error('Response not "OK"')
            }
        } catch (error) {
            console.error('error', error)
        }
    }
}

import {useEffect, useState} from "react"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react"
import { useNavigate } from "react-router-dom"


function JournalList() {
    const [journals, setJournals] = useState([])
    const {token} = useAuthContext()
    const navigate = useNavigate();
    const [isLoading, setIsLoading] = useState(true)

    const getUserIdFromToken = async (token) => {
        try {
            const tokenUrl = `${process.env.VITE_REACT_APP_API_HOST}/token`
            const response = await fetch(tokenUrl, {
                headers: { "Authorization": `Bearer ${token}` },
                credentials : "include" ,
            })
            if (response.ok) {
                const data =await response.json()
            } else {
                console.error("Request error:", response.status)
            }
        } catch (e) {
            console.error("An error occured with request:", e);
        }
    }

    const getData = async () => {
        setIsLoading(true)
        try {
            const journalUrl = `${process.env.VITE_REACT_APP_API_HOST}/journals`
            const response = await fetch(journalUrl, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (response.ok) {
                const data = await response.json()
                setJournals(data)
            } else {
                console.error("Request error:", response.status)
            }
        } catch (e) {
            console.error("An error occured with request:", e)
        } finally {
            setIsLoading(false)
        }
    }

    const handleDetailClick = (journal) => {
        const user_id = getUserIdFromToken(token)
        navigate(`/journal/${journal.id}?user_id=${user_id}`)
    }

    useEffect(() => {
        getData(),
        getUserIdFromToken()
    }, [token])

        return (
        <div>
            <h1>Journals</h1>
            <table className="table table-striped">
                <thead>
                <tr>
                    <th>Location</th>
                    <th>Picture URL</th>
                    <th>Description</th>
                    <th>Rating</th>
                    <th>Date</th>
                </tr>
                </thead>
                <tbody>
                {journals.map(journal => {
                    return (
                    <tr key={journal.id}>
                        <td>{journal.location}</td>
                        <td>{journal.picture_url}</td>
                        <td>{journal.description}</td>
                        <td>{journal.rating}</td>
                        <td>{journal.date}</td>
                        <td>
                            <button onClick={() => handleDetailClick(journal)}
                            className="btn btn-primary"
                            >
                                View my Journal Entry
                            </button>
                        </td>
                    </tr>
                    );
                })}
                </tbody>
            </table>
        </div>
        )
    }
    export default JournalList

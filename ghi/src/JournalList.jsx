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
            const tokenUrl = `http://localhost:8000/token`
            const response = await fetch(tokenUrl, {
                headers: { "Authorization": `Bearer ${token}` },
                credentials : "include" , 
            })
            if (response.ok) {
                const data =await response.json()
            } else {
            }
        } catch (e) {
        }        
    }

    const getData = async () => {
        setIsLoading(true)
        try {
            const journalUrl = 'http://localhost:8000/journals'
            const response = await fetch(journalUrl, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (response.ok) {
                const data = await response.json()
                setJournals(data)
            } else {
            }
        } catch (e) {
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
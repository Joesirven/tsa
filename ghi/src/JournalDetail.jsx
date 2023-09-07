import {useEffect, useState} from "react"
import useToken, { useAuthContext } from "@galvanize-inc/jwtdown-for-react"
import { useParams } from "react-router-dom"


function JournalDetail() {
    const {token} = useToken()
    const [isLoading, setIsLoading] = useState(true)
    const [journal, setJournal] = useState([])
    const { id } = useParams()


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
                console.error("Request error:", response.status)
            }
        } catch (e) {
            console.error("An error occured with request:", e);
        }        
    }
        
    const getData = async () => {
        setIsLoading(true)
        try {
            const journalUrl = `http://localhost:8000/journal/${id}`;
            const response = await fetch(journalUrl, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (response.ok) {
                const data = await response.json()
                setJournal(data)
            } else {
                console.error("Request error:", response.status)
            }
        } catch (e) {
            console.error("An error occured with request:", e)
        } finally {
            setIsLoading(false)
        }
    }

    useEffect(() => {
        getData(),
        getUserIdFromToken()
    }, [token])

        return (
            <div>
                <h1>Journal Details</h1>
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
                    <tr key={journal.id}>
                        <td>{journal.location}</td>
                        <td>{journal.picture_url}</td>
                        <td>{journal.description}</td>
                        <td>{journal.rating}</td>
                        <td>{journal.date}</td>
                    </tr>
                </tbody>
                </table>
                <div>
                    <button>Edit</button>
                </div>                   
            </div>
        );
    }
    export default JournalDetail;
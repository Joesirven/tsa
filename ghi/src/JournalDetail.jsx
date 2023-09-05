import {useEffect, useState} from "react"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";


function JournalDetail() {
    const [journal, setJournal] = useState([])
    const {token} = useAuthContext()

    const getData = async () => {
        const journalUrl = `http://localhost:8000/journal/${journal_id}`;
        try {
            const response = await fetch(journalUrl, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (response.ok) {
                const data = await response.json();
                setJournal(data.journal)
            } else {
                console.error("Request error:", response.status)
            }
        } catch (e) {
            console.error("An error occured with request:", e)
        }    
    }
    useEffect(() => {
        getData()
    }, [])

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
        </div>
        )
    }
    export default JournalDetail;
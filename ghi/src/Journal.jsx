import {useEffect, useState} from "react"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";


function JournalList() {
    const [journals, setJournals] = useState([])
    const {token} = useAuthContext
    const getData = async () => {
        const journalUrl = 'http://localhost:8000/journals'
        try {
            const response = await fetch(journalUrl, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (response.ok) {
                const data = await response.json();
                setJournals(data.journals)
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
                    </tr>
                    );
                })}
                </tbody>
            </table>
        </div>
        )
    }
    export default JournalList
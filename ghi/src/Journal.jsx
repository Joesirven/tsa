import {useEffect, useState} from "react"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";


function SomeComponent() {
  const { token } = useAuthContext();
}

const request = await fetch(url, {
  headers: { Authorization: `Bearer ${token}` },
  // Other fetch options, like method and body, if applicable
});


function JournalList() {
    const [getJournals, setJournal] = useState([])
    const getData = async () => {
        const journalUrl = 'http://localhost:8000/journals'
        try {
            const response = await fetch(journalUrl)
            console.log(response)
            if (response.ok) {
                const data = await response.json();
                console.log(data)
                setJournal(data.journals)
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
                {getJournals.map(journals => {
                    return (
                    <tr key={journals.id}>
                        <td>{journals.location}</td>
                        <td>{journals.picture_url}</td>
                        <td>{journals.description}</td>
                        <td>{journals.rating}</td>
                        <td>{journals.date}</td>
                    </tr>
                    );
                })}
                </tbody>
            </table>
        </div>
        )
    }
    export default JournalList
import {useEffect, useState} from "react"

function JournalList() {
    const [getJournals, setJournal] = useState([])
    const getData = async () => {
        const journalUrl = 'http://localhost:8000/journals'
        const response = await fetch(journalUrl)
        
        if (response.ok) {
        const data = await response.json();
        setJournal(data.journals)
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
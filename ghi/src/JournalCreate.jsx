import {useState} from "react"

function JournalCreate() {
    const [formData, setFormData] = useState({
        location: '',
        picture_url: '',
        description: '',
        rating: '',
        date: '',
    })
    const handleSubmit = asyn (e) => {
        e.preventDefault()
        const journalUrl = 'http://localhost:8000/journal'
        const fetchConfig = {
            method: 'POST',
            body: JSON.stringify(formData),
            headers: {
                "Content-Type": 'application/json',
            },
        }
        const response = await fetch(journalUrl, fetchConfig)
        if (response.ok) {
            setFormData({
                location: '',
                picture_url: '',
                description: '',
                rating: '',
                date: '',
            })
        }
    }
    const handleFormChange = (e) => {
        const value = e.target.value
        const inputJournal = e.target.name
        setFormData({
            ...formData,
            [inputJournal]: value
        })
    }
    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create a new journal entry</h1>
                        <form onSubmit={handleSubmit} id="create-journal-form">           
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.location} placeholder="Enter Location" required type="text" name="location" id="location" className="form-control" />
                            <label htmlFor="location">Location</label>
                        </div>          
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.picture_url} placeholder="Enter picture url" required type="text" name="picture_url" id="picture_url" className="form-control" />
                            <label htmlFor="picture_url">Picture Url</label>
                        </div>           
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.description} placeholder="Enter description" required type="text" name="description" id="description" className="form-control" />
                            <label htmlFor="description">Description</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.rating} placeholder="Enter rating" required type="text" name="rating" id="rating" className="form-control" />
                            <label htmlFor="rating">Rating</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.date} placeholder="Enter date" required type="text" name="date" id="date" className="form-control" />
                            <label htmlFor="date">Date</label>
                        </div>
                        <button className="btn btn-primary">Create New Journal</button>
                    </form>
                </div>
            </div>
        </div>
    )
}
export default function CreateProject({ handleSubmit, inputValue, handleInputChange }) {

  return (
    <div >
      <main >
        <h1 >Create a new project</h1>
        <p >
          Create new project, upload documents and Ask questions about the data of the documents.
        </p>
        <div >
          <input
            type="text"
            placeholder="Ask GenDoncs for software project title..."
            value={inputValue} 
            onChange={handleInputChange} 
          />
          <button  onClick={handleSubmit}>↗</button> {/* Trigger POST on click */}
        </div>
      </main>
      <footer >
        <a href="/faq" >FAQ</a>
        <a href="/terms" >Terms</a>
        <a href="/privacy" >Privacy</a>
      </footer>
    </div>
  );
}

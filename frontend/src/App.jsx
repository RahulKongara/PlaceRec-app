import { useState } from "react";    
import { TfiAlert } from "react-icons/tfi";
import Upload from "./components/Upload";      
import Results from "./components/Results";    

export default function App() {
  const [data, setData] = useState(null);


  const handleResult = (result) => {
    setData(result);
  };

  return (
    <div className="app-container">
      <header>
        <h1>AI Travel Advisor</h1>
      </header>

      <main>
        <Upload onResult={handleResult} />

        <Results data={data} />
      </main>
      <TfiAlert size={20} className="icon" />
      <p className="dev-msg">Keep in mind that this site is still under maintenance</p>
      <footer>
        <p>© 2025 Travel Advisor</p>
      </footer>
    </div>
  );
}

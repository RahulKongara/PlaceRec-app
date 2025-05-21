export default function Results({ data }) {
    if (!data) return null;
    const { identified, recommendations } = data;
    return (
        <div className="results-container">
            <h2>Identified: {identified.name}</h2>
            <h5>Location: {identified.location}</h5>
            <p>{identified.description}</p>
            <h3>Recommended Next Spots: </h3>
            <ul>
                {recommendations.map(r => (
                    <li key={r.id}>
                        <strong>{r.name}</strong> - {r.location}
                    </li>
                ))}
            </ul>
        </div>
    );
}
import EstimateSummaryCard, {
  transformToEstimateSummary,
} from "../../dto/estimateSummary.tsx";
import rawData from "../../data/raw.json";

export default function App() {
  const summary = transformToEstimateSummary(rawData);
  return (
    <div>
      <EstimateSummaryCard summary={summary} />
    </div>
  );
}

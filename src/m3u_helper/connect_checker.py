from typing import Dict, List, Tuple
import requests
from concurrent import futures
from tqdm import tqdm


class ConnectChecker:
    @classmethod
    def __check(cls, uri: str):
        try:
            r = requests.get(uri, timeout=0.1, stream=True)
        except requests.exceptions.Timeout:
            return False
        except Exception:
            return False
        else:
            if r.status_code == 200:
                return True
            else:
                return False

    @classmethod
    def checkURIs(cls, uris: Tuple[str]) -> Dict[str, bool]:
        MAX_SAME_TIME_DEAL = 10
        maxWorkers = min(MAX_SAME_TIME_DEAL, len(uris))
        connResults = {}
        with futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
            futureMap = {}
            for uri in uris:
                future = executor.submit(cls.__check, uri)
                futureMap[future] = uri
            futureDone = futures.as_completed(futureMap)
            for future in tqdm(futureDone, total=len(uris)):
                isConnect = future.result()
                connResults[futureMap[future]] = isConnect
        return connResults

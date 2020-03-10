from typing import List

from numpy.core._multiarray_umath import ndarray

from src.scan_faces._embedder.embedder import calculate_embedding
from src.scan_faces._detector.constants import FaceLimit, FaceLimitConstant, DEFAULT_THRESHOLD_C
from src.scan_faces._detector.detector import detect_faces
from src.scan_faces.dto.face import ScannedFace, DetectedFace


def _get_scanned_face(img: ndarray, detected_face: DetectedFace) -> ScannedFace:
    embedding = calculate_embedding(img, detected_face.box)
    return ScannedFace(embedding=embedding, **detected_face.__dict__)


def scan_faces(img: ndarray, face_limit: FaceLimit = FaceLimitConstant.NO_LIMIT,
               detection_threshold_c: float = DEFAULT_THRESHOLD_C) -> \
        List[ScannedFace]:
    detected_faces = detect_faces(img, face_limit, detection_threshold_c)
    scanned_faces = [_get_scanned_face(img, detected_face) for detected_face in detected_faces]
    return scanned_faces

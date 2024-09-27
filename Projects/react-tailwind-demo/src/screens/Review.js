import React, { useState } from 'react';
import { FaChevronLeft, FaEllipsisV } from 'react-icons/fa';

const ReviewModal = ({ isOpen, onClose, onSubmit }) => {
    const [reviewText, setReviewText] = useState('');

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 flex justify-center items-center p-4">
            <div className="bg-white p-4 rounded-lg shadow-lg space-y-4">
                <textarea
                    className="w-full p-2 border border-gray-300 rounded"
                    value={reviewText}
                    onChange={(e) => setReviewText(e.target.value)}
                    placeholder="Write your review..."
                />
                <button
                    className="bg-blue-500 text-white p-2 rounded"
                    onClick={() => {
                        onSubmit(reviewText);
                        onClose();
                    }}
                >
                    Submit Review
                </button>
            </div>
        </div>
    );
};

const Review = () => {
    const reviews = [
        {
            id: 1,
            name: "Nathasa Malkuba",
            date: "28/02/2021",
            review: "Loved the class! Such beautiful land and collective impact infrastructure social entrepreneurship mass incarceration 👍",
            rating: 5.0
        },
        {
            id: 2,
            name: "Furinai Millabi",
            date: "01/03/2021",
            review: "Never run so well and it’s all thanks to Jordan. Silo framework overcome justice ideate, citizen-centered effective",
            rating: 4.0
        },
        {
            id: 3,
            name: "Sami Rafi",
            date: "01/03/2021",
            review: "Big up my running crew, they better not say running crew who! Commitment equal opportunity empower.",
            rating: 4.5
        }
    ];
    const [modalOpen, setModalOpen] = useState(false);

    const handleReviewSubmit = (review) => {
        console.log("Review Submitted: ", review); // Handle review submission
    };

    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
                <FaChevronLeft className="cursor-pointer text-gray-600" onClick={() => console.log('Go Back')} />
                <h1 className="text-xl font-bold">Review</h1>
                <FaEllipsisV className="cursor-pointer text-gray-600" />
            </div>
            {/* Review list here */}
            <div className="space-y-4">
                {reviews.map(review => (
                    <div key={review.id} className="bg-white p-4 rounded-lg shadow-md">
                        <div className="flex justify-between items-center">
                            <div>
                                <h5 className="font-bold">{review.name}</h5>
                                <p className="text-sm text-gray-500">{review.date}</p>
                            </div>
                            <FaEllipsisV className="cursor-pointer text-gray-500" />
                        </div>
                        <p className="mt-2">{review.review}</p>
                    </div>
                ))}
            </div>
            <button
                className="mt-6 bg-blue-500 text-white p-3 rounded-lg w-full"
                onClick={() => setModalOpen(true)}
            >
                Write your review...
            </button>
            <ReviewModal
                isOpen={modalOpen}
                onClose={() => setModalOpen(false)}
                onSubmit={handleReviewSubmit}
            />
        </div>
    );
};

export default Review;
